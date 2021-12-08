# text taken from https://www.greenshareenergy.com/blog/what-are-agrivoltaics
text = "More broadly, agrivoltaic systems create a number of dual-use synergies between the solar panels and agricultural crops, which unlocks benefits for all aspects of the system: solar panel PV performance, crop yields, and economic benefits for the farmer. Solar PV panel performance increases for a number of reasons. Firstly, because the panels are placed above the crops, this means they are farther off the ground (and closer to the sun) so they will have increased efficiency of power generation. Secondly, because the land under the solar panel is now cropland, it stays cooler and prevents the ground under the solar panel from heating up too much, which in turn increases the efficiency of the solar panel. Agrivoltaic systems also generate significant benefits for crop yield. The solar panels can function as a protective foil, decreasing the destructive impacts of weather and wind on crop yield. Furthermore, the solar panels can be placed in a way to optimize light availability for the crops. Finally, agrivoltaic systems introduce a number of direct economic benefits for farmers (aside from the cheap irrigation process described above). The presence of the solar panel can actually reduce unnecessary wind and solar radiation impacts on crops, which enables them to better retain water, which reduces the need for irrigation for farmers. The solar panels can also collect rainwater, which can further decrease irrigation costs. Finally, the presence of solar panels will increase property values for the land, which could enable the farmer to sell for a higher value. All of these benefits showcase the dual-use synergies between solar PV panels and agricultural operations present within an agrivoltaic system. In fact, pilot projects have shown substantial land use efficiency increases as a result of installing agrivoltaic systems (ranging from 60% to 186% increase) There is no doubt that we must scale up this application here in the US."

def word_count(text: str):
    _list = text.split(" ")
    return len(_list)

print(word_count(text))