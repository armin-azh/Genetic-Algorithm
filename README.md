# Genetic-Algorithm
<p>providing genetic algorithm for problems</p>
<p>this algorithm is now in developing mode</p>
<h2 style="color:green">and it solves:</h2>
<p>finding extermum value of the specific funtion</p>

# How to Use:
in tools.py
<ul>
  <li>get_bin_value() // getting the binary value</li>
  <li>map_binary_value_to_domain() //maping the value of the binary array to the range of the domain</li>
  <li>find_bits_for_accurct() //finiding needs bit for genes in chromosome</li>
  <li>convert_binary_to_gray() //converting binay code to gray code</li>
  <li>conver_gray_to_binary() //converting gray code to binary code</li>
  <li>choice_zero_or_one() //random 0 or 1 value</li>
  <li>choice_int_between_a_and_b() //random int value between [a,b]</li>
  <li>choice_float_between_zero_and_one() //float random value between 0 or 1</li>
  <li>single_point_crossover() //crossover opration</li>
  <li>calculate_roullet_wheel() //random selection</li>
  <li>calculate_searching_space_accurcy() //calculate accuracy of the defined space</li>
</ul>

in scaling_tool.py:
<p>we provide some scaling tool for scaling the fitness function value</p>
<ul>
  <li>linear_scaling()</li>
  <li>dynamic_linear_scaling</li>
  <li>pow_scaling</li>
  <li>logarithm_scaling</li>
  <li>nomalization</li>
</ul>


in GA.py:
we defined main class
<ul>
  <li>Chromosome:</li>
  <li>Generation:</li>
  <li>Genetic:</li>
</ul>


<h3>for using use custom GA algoritm you can have your main() methon in Genetic class</h3>

the parameter that you can tune it:
<ul>
  <li>number_of_papulation //Number of the papulation for starting</li>
  <li>function //your specific function</li>
  <li>fitness_function //custom fitness function</li>
  <li>domain //input space</li>
  <li>mutation_rate //mutation rate(default is 0)</li>
  <li>crossover_rate//crossover rate (default is 1)</li>
  <li>mutation_bit //number of genes bit that you want to do the mutation oprand</li>
  <li>accurcy //accuracy of the genes value</li>
</ul>
