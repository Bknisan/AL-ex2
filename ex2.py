import csv
import math


def information_gain():
    return 0


def entropy(class_1, class_2):
    return ((-class_1 / (class_1 + class_2)) * math.log2((class_1 / (class_1 + class_2))) - (
            (class_2 / (class_1 + class_2)) * math.log2(class_2 / (class_1 + class_2))))


def separate_by_classification(data_set):
    classification_1 = data_set[0][-1]
    first_class = []
    second_class = []
    for instance in data_set:
        if instance[-1] == classification_1:
            first_class.append(instance)
        else:
            second_class.append(instance)
    separated = {first_class[-1][-1]: first_class, second_class[-1][-1]: second_class}
    return separated


def calc_tag_ratio(separated_set, data_set):
    rate = {}
    for tag, instances in separated_set.items():
        rate[tag] = len(instances) / len(data_set)
    return rate


def key_with_max_val(dic):
    v = list(dic.values())
    k = list(dic.keys())
    return k[v.index(max(v))]


def read_data():
    # open the data set and go to start.
    file = open("dataset.txt", 'r')
    file.seek(0)
    # read as CSV with tab as a deli
    r = csv.reader(file, delimiter='\t')
    return list(r)[1:]


# decision tree printer as wished.
def dt_printer():
    return 0


# todo: finish last algorithm
def id3(separated_instances):
    keys = list(separated_instances.keys())
    set_entropy = entropy(len(separated_instances[keys[0]]), len(separated_instances[keys[1]]))
    return set_entropy


def multiple_list(my_list):
    base = 1
    for element in my_list:
        base *= element
    return base


def naive_base(separated_set, speculate, data_set):
    attributes_probs_by_class = {}
    for index in range(len(speculate)):
        for tag, instances in separated_set.items():
            if tag not in attributes_probs_by_class:
                attributes_probs_by_class[tag] = []
            similarities = 0
            for instance in instances:
                if instance[index] == speculate[index]:
                    similarities += 1
            att_prob = similarities / len(instances)
            attributes_probs_by_class[tag].append(att_prob)

    class_chances = {}
    # calculate class ratio
    ratio = calc_tag_ratio(separated_set, data_set)
    for tag in attributes_probs_by_class:
        if tag not in class_chances:
            # multiply all att similarities by tag.
            class_chances[tag] = (multiple_list(attributes_probs_by_class[tag]) * ratio[tag]) * 100
    return key_with_max_val(class_chances)


# the less the distance the similar the objects
def hemming_dis(x, y):
    distance = 0
    for iks, uay in zip(x, y):
        if iks != uay:
            distance += 1
    return distance


# done
# return values and their distance from candidate
def knn(data_set, candidate):
    nearest_distance = [104, 103, 102, 101, 100]
    nearest_values = [0, 0, 0, 0, 0]
    for instance in data_set:
        distance = hemming_dis(instance, candidate)
        if distance < max(nearest_distance):
            index = nearest_distance.index(max(nearest_distance))
            nearest_distance[index] = distance
            nearest_values[index] = instance
    return [nearest_values, nearest_distance]


if __name__ == '__main__':
    train = read_data()
    separated_by_class = separate_by_classification(train)
    id3(separated_by_class)
    # check function
#   print(naive_base(separated_by_class, train[0][:len(train[0]) - 1], train[:4]))
#   nearest_neighbours = knn(train, train[123])
#   print(nearest_neighbours)
