import numpy as np

marks = np.array([
    [80, 85, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68]
])

print("Marks:")
print(marks)

print("Shape:", marks.shape)

print("Overall mean:", np.mean(marks))
print("Subject-wise mean:", np.mean(marks, axis=0))
print("Student-wise mean:", np.mean(marks, axis=1))

print("Subject-wise minimum:", np.min(marks, axis=0))
print("Subject-wise maximum:", np.max(marks, axis=0))
print("Subject-wise range:", np.max(marks, axis=0) - np.min(marks, axis=0))
