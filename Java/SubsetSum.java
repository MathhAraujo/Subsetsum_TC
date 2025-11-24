package Java;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class SubsetSum {

    static List<List<Integer>> solutions = new ArrayList<>();

public static void main(String[] args) {
        String inputFolder = "Input/";   
        String resultsFile = "Results/results.xlsx"; 

        executeFile(inputFolder + "small_input.txt", resultsFile);
        executeFile(inputFolder + "med_input.txt", resultsFile);
        executeFile(inputFolder + "big_input.txt", resultsFile);
    }

    public static List<List<Integer>> subsetSum(List<Integer> numbers, int target) {
        solutions = new ArrayList<>();
        search(0, 0, new ArrayList<>(), numbers, target);
        return solutions;
    }

    private static void search(int index, int currentSum, List<Integer> currentList, List<Integer> numbers, int target) {
        if (currentSum == target) {
            if (!solutions.contains(currentList)) {
                solutions.add(new ArrayList<>(currentList));
                return;
            }
        }

        if (index >= numbers.size() || currentSum > target) {
            return;
        }

        int currentNum = numbers.get(index);
        currentList.add(currentNum);

        search(index + 1, currentSum + currentNum, currentList, numbers, target);

        currentList.remove(currentList.size() - 1);

        search(index + 1, currentSum, currentList, numbers, target);
    }

    public static void executeFile(String samplePath, String resultPath) {
        List<String> languageList = new ArrayList<>();
        List<Integer> inputSizeList = new ArrayList<>();
        List<Integer> targetList = new ArrayList<>();
        List<String> executionTimeList = new ArrayList<>();

        try {
            List<String> data = Files.readAllLines(Paths.get(samplePath));

            for (int i = 0; i < data.size() / 3; i++) {
                try {
                    String targetLine = data.get(i * 3).trim();
                    if (targetLine.isEmpty() || targetLine.equals("---")) continue;

                    int target = Integer.parseInt(targetLine);
                    
                    String numbersLine = data.get(i * 3 + 1).trim();
                    List<Integer> numbers = new ArrayList<>();
                    
                    if (!numbersLine.isEmpty()) {
                        for (String s : numbersLine.split(" ")) {
                            numbers.add(Integer.parseInt(s));
                        }
                    }

                    languageList.add("Java");
                    inputSizeList.add(numbers.size());
                    targetList.add(target);

                    long start = System.nanoTime();
                    subsetSum(numbers, target);
                    long end = System.nanoTime();

                    double durationMs = (end - start) / 1_000_000.0;
                    executionTimeList.add(String.format(Locale.US, "%.4f", durationMs));

                } catch (NumberFormatException | IndexOutOfBoundsException e) {
                }
            }

            File file = new File(resultPath);
            Workbook workbook;
            Sheet sheet;

            if (file.exists()) {
                FileInputStream fis = new FileInputStream(file);
                workbook = new XSSFWorkbook(fis);
                sheet = workbook.getSheetAt(0);
                fis.close();
            } else {
                workbook = new XSSFWorkbook();
                sheet = workbook.createSheet("Results");
                Row header = sheet.createRow(0);
                header.createCell(0).setCellValue("language");
                header.createCell(1).setCellValue("input_size");
                header.createCell(2).setCellValue("target");
                header.createCell(3).setCellValue("execution_time");
            }

            int rowNum = sheet.getLastRowNum() + 1;

            for (int j = 0; j < languageList.size(); j++) {
                Row row = sheet.createRow(rowNum++);
                row.createCell(0).setCellValue(languageList.get(j));
                row.createCell(1).setCellValue(inputSizeList.get(j));
                row.createCell(2).setCellValue(targetList.get(j));

                row.createCell(3).setCellValue(executionTimeList.get(j));
            }

            FileOutputStream fos = new FileOutputStream(file);
            workbook.write(fos);
            workbook.close();
            fos.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}