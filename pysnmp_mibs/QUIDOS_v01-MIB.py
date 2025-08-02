_I='device_msg'
_H='user_name'
_G='NotificationType'
_F='index'
_E='read-only'
_D='QUIDOS_v01-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class OnOff(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
class StatCit(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('falling',1),('rising',2),('both',3)))
_PapouchProjekt_ObjectIdentity=ObjectIdentity
papouchProjekt=_PapouchProjekt_ObjectIdentity((1,3,6,1,4,1,18248))
_Quidos_ObjectIdentity=ObjectIdentity
quidos=_Quidos_ObjectIdentity((1,3,6,1,4,1,18248,16))
_Quido_var_ObjectIdentity=ObjectIdentity
quido_var=_Quido_var_ObjectIdentity((1,3,6,1,4,1,18248,16,1))
_TemperatureReading_Type=Integer32
_TemperatureReading_Object=MibScalar
temperatureReading=_TemperatureReading_Object((1,3,6,1,4,1,18248,16,1,1),_TemperatureReading_Type())
temperatureReading.setMaxAccess(_E)
if mibBuilder.loadTexts:temperatureReading.setStatus(_A)
_Temperature_S_Reading_Type=DisplayString
_Temperature_S_Reading_Object=MibScalar
temperature_S_Reading=_Temperature_S_Reading_Object((1,3,6,1,4,1,18248,16,1,2),_Temperature_S_Reading_Type())
temperature_S_Reading.setMaxAccess(_E)
if mibBuilder.loadTexts:temperature_S_Reading.setStatus(_A)
_User_name_Type=DisplayString
_User_name_Object=MibScalar
user_name=_User_name_Object((1,3,6,1,4,1,18248,16,1,3),_User_name_Type())
user_name.setMaxAccess(_B)
if mibBuilder.loadTexts:user_name.setStatus(_A)
_Device_msg_Type=DisplayString
_Device_msg_Object=MibScalar
device_msg=_Device_msg_Object((1,3,6,1,4,1,18248,16,1,4),_Device_msg_Type())
device_msg.setMaxAccess(_E)
if mibBuilder.loadTexts:device_msg.setStatus(_A)
_Table_in_ObjectIdentity=ObjectIdentity
table_in=_Table_in_ObjectIdentity((1,3,6,1,4,1,18248,16,2))
_InTable_Object=MibTable
inTable=_InTable_Object((1,3,6,1,4,1,18248,16,2,1))
if mibBuilder.loadTexts:inTable.setStatus(_A)
_InEntry_Object=MibTableRow
inEntry=_InEntry_Object((1,3,6,1,4,1,18248,16,2,1,1))
inEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:inEntry.setStatus(_A)
__pysmi_in_Type=OnOff
__pysmi_in_Object=MibTableColumn
_pysmi_in=__pysmi_in_Object((1,3,6,1,4,1,18248,16,2,1,1,1),__pysmi_in_Type())
_pysmi_in.setMaxAccess(_E)
if mibBuilder.loadTexts:_pysmi_in.setStatus(_A)
_In_name_Type=DisplayString
_In_name_Object=MibTableColumn
in_name=_In_name_Object((1,3,6,1,4,1,18248,16,2,1,1,2),_In_name_Type())
in_name.setMaxAccess(_B)
if mibBuilder.loadTexts:in_name.setStatus(_A)
_CitrwS_Type=StatCit
_CitrwS_Object=MibTableColumn
citrwS=_CitrwS_Object((1,3,6,1,4,1,18248,16,2,1,1,3),_CitrwS_Type())
citrwS.setMaxAccess(_B)
if mibBuilder.loadTexts:citrwS.setStatus(_A)
class _Citrw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Citrw_Type.__name__=_C
_Citrw_Object=MibTableColumn
citrw=_Citrw_Object((1,3,6,1,4,1,18248,16,2,1,1,4),_Citrw_Type())
citrw.setMaxAccess(_B)
if mibBuilder.loadTexts:citrw.setStatus(_A)
_Table_out_ObjectIdentity=ObjectIdentity
table_out=_Table_out_ObjectIdentity((1,3,6,1,4,1,18248,16,3))
_OutTable_Object=MibTable
outTable=_OutTable_Object((1,3,6,1,4,1,18248,16,3,1))
if mibBuilder.loadTexts:outTable.setStatus(_A)
_OutEntry_Object=MibTableRow
outEntry=_OutEntry_Object((1,3,6,1,4,1,18248,16,3,1,1))
outEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:outEntry.setStatus(_A)
_Out_Type=OnOff
_Out_Object=MibTableColumn
out=_Out_Object((1,3,6,1,4,1,18248,16,3,1,1,1),_Out_Type())
out.setMaxAccess(_B)
if mibBuilder.loadTexts:out.setStatus(_A)
_Out_name_Type=DisplayString
_Out_name_Object=MibTableColumn
out_name=_Out_name_Object((1,3,6,1,4,1,18248,16,3,1,1,2),_Out_name_Type())
out_name.setMaxAccess(_B)
if mibBuilder.loadTexts:out_name.setStatus(_A)
_OutTwr_Type=Integer32
_OutTwr_Object=MibTableColumn
outTwr=_OutTwr_Object((1,3,6,1,4,1,18248,16,3,1,1,3),_OutTwr_Type())
outTwr.setMaxAccess(_B)
if mibBuilder.loadTexts:outTwr.setStatus(_A)
_Table_term_ObjectIdentity=ObjectIdentity
table_term=_Table_term_ObjectIdentity((1,3,6,1,4,1,18248,16,4))
_TermTable_Object=MibTable
termTable=_TermTable_Object((1,3,6,1,4,1,18248,16,4,1))
if mibBuilder.loadTexts:termTable.setStatus(_A)
_TermEntry_Object=MibTableRow
termEntry=_TermEntry_Object((1,3,6,1,4,1,18248,16,4,1,1))
termEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:termEntry.setStatus(_A)
class _ModeTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_ModeTerm_Type.__name__=_C
_ModeTerm_Object=MibTableColumn
modeTerm=_ModeTerm_Object((1,3,6,1,4,1,18248,16,4,1,1,1),_ModeTerm_Type())
modeTerm.setMaxAccess(_B)
if mibBuilder.loadTexts:modeTerm.setStatus(_A)
class _MezHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_MezHi_Type.__name__=_C
_MezHi_Object=MibTableColumn
mezHi=_MezHi_Object((1,3,6,1,4,1,18248,16,4,1,1,2),_MezHi_Type())
mezHi.setMaxAccess(_B)
if mibBuilder.loadTexts:mezHi.setStatus(_A)
class _MezLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-550,1250))
_MezLo_Type.__name__=_C
_MezLo_Object=MibTableColumn
mezLo=_MezLo_Object((1,3,6,1,4,1,18248,16,4,1,1,3),_MezLo_Type())
mezLo.setMaxAccess(_B)
if mibBuilder.loadTexts:mezLo.setStatus(_A)
class _Time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Time_Type.__name__=_C
_Time_Object=MibTableColumn
time=_Time_Object((1,3,6,1,4,1,18248,16,4,1,1,4),_Time_Type())
time.setMaxAccess(_B)
if mibBuilder.loadTexts:time.setStatus(_A)
class _Err_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Err_Type.__name__=_C
_Err_Object=MibTableColumn
err=_Err_Object((1,3,6,1,4,1,18248,16,4,1,1,5),_Err_Type())
err.setMaxAccess(_B)
if mibBuilder.loadTexts:err.setStatus(_A)
temp_msg=NotificationType((1,3,6,1,4,1,18248,16,1,0,1))
temp_msg.setObjects(*((_D,_H),(_D,_I)))
if mibBuilder.loadTexts:temp_msg.setStatus('')
mibBuilder.exportSymbols(_D,**{'PositiveInteger':PositiveInteger,'OnOff':OnOff,'StatCit':StatCit,'papouchProjekt':papouchProjekt,'quidos':quidos,'quido_var':quido_var,'temp_msg':temp_msg,'temperatureReading':temperatureReading,'temperature_S_Reading':temperature_S_Reading,_H:user_name,_I:device_msg,'table_in':table_in,'inTable':inTable,'inEntry':inEntry,'in':_pysmi_in,'in_name':in_name,'citrwS':citrwS,'citrw':citrw,'table_out':table_out,'outTable':outTable,'outEntry':outEntry,'out':out,'out_name':out_name,'outTwr':outTwr,'table_term':table_term,'termTable':termTable,'termEntry':termEntry,'modeTerm':modeTerm,'mezHi':mezHi,'mezLo':mezLo,'time':time,'err':err})