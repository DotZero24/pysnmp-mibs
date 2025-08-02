_H='psAlarmString'
_G='deviceName'
_F='mandatory'
_E='NotificationType'
_D='Integer32'
_C='Th2e-v01-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PapouchProjekt_ObjectIdentity=ObjectIdentity
papouchProjekt=_PapouchProjekt_ObjectIdentity((1,3,6,1,4,1,18248))
_The_ObjectIdentity=ObjectIdentity
the=_The_ObjectIdentity((1,3,6,1,4,1,18248,20))
_Version1_ObjectIdentity=ObjectIdentity
version1=_Version1_ObjectIdentity((1,3,6,1,4,1,18248,20,1))
_Device_var_ObjectIdentity=ObjectIdentity
device_var=_Device_var_ObjectIdentity((1,3,6,1,4,1,18248,20,1,1))
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,18248,20,1,1,1),_DeviceName_Type())
deviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceName.setStatus(_F)
_PsAlarmString_Type=DisplayString
_PsAlarmString_Object=MibScalar
psAlarmString=_PsAlarmString_Object((1,3,6,1,4,1,18248,20,1,1,2),_PsAlarmString_Type())
psAlarmString.setMaxAccess(_B)
if mibBuilder.loadTexts:psAlarmString.setStatus(_F)
_Table_channel_ObjectIdentity=ObjectIdentity
table_channel=_Table_channel_ObjectIdentity((1,3,6,1,4,1,18248,20,1,2))
_ChannelTable_Object=MibTable
channelTable=_ChannelTable_Object((1,3,6,1,4,1,18248,20,1,2,1))
if mibBuilder.loadTexts:channelTable.setStatus(_A)
_ChannelEntry_Object=MibTableRow
channelEntry=_ChannelEntry_Object((1,3,6,1,4,1,18248,20,1,2,1,1))
channelEntry.setIndexNames((0,_C,'index'))
if mibBuilder.loadTexts:channelEntry.setStatus(_A)
_InChStatus_Type=Integer32
_InChStatus_Object=MibTableColumn
inChStatus=_InChStatus_Object((1,3,6,1,4,1,18248,20,1,2,1,1,1),_InChStatus_Type())
inChStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:inChStatus.setStatus(_A)
_InChValue_Type=Integer32
_InChValue_Object=MibTableColumn
inChValue=_InChValue_Object((1,3,6,1,4,1,18248,20,1,2,1,1,2),_InChValue_Type())
inChValue.setMaxAccess(_B)
if mibBuilder.loadTexts:inChValue.setStatus(_A)
_InChUnits_Type=Integer32
_InChUnits_Object=MibTableColumn
inChUnits=_InChUnits_Object((1,3,6,1,4,1,18248,20,1,2,1,1,3),_InChUnits_Type())
inChUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:inChUnits.setStatus(_A)
_Table_watchValue_ObjectIdentity=ObjectIdentity
table_watchValue=_Table_watchValue_ObjectIdentity((1,3,6,1,4,1,18248,20,1,3))
_WatchValTable_Object=MibTable
watchValTable=_WatchValTable_Object((1,3,6,1,4,1,18248,20,1,3,1))
if mibBuilder.loadTexts:watchValTable.setStatus(_A)
_WatchValEntry_Object=MibTableRow
watchValEntry=_WatchValEntry_Object((1,3,6,1,4,1,18248,20,1,3,1,1))
watchValEntry.setIndexNames((0,_C,'index'))
if mibBuilder.loadTexts:watchValEntry.setStatus(_A)
class _ModeWatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ModeWatch_Type.__name__=_D
_ModeWatch_Object=MibTableColumn
modeWatch=_ModeWatch_Object((1,3,6,1,4,1,18248,20,1,3,1,1,1),_ModeWatch_Type())
modeWatch.setMaxAccess(_B)
if mibBuilder.loadTexts:modeWatch.setStatus(_A)
_LimitHi_Type=Integer32
_LimitHi_Object=MibTableColumn
limitHi=_LimitHi_Object((1,3,6,1,4,1,18248,20,1,3,1,1,2),_LimitHi_Type())
limitHi.setMaxAccess(_B)
if mibBuilder.loadTexts:limitHi.setStatus(_A)
_LimitLo_Type=Integer32
_LimitLo_Object=MibTableColumn
limitLo=_LimitLo_Object((1,3,6,1,4,1,18248,20,1,3,1,1,3),_LimitLo_Type())
limitLo.setMaxAccess(_B)
if mibBuilder.loadTexts:limitLo.setStatus(_A)
_LimitHy_Type=Integer32
_LimitHy_Object=MibTableColumn
limitHy=_LimitHy_Object((1,3,6,1,4,1,18248,20,1,3,1,1,4),_LimitHy_Type())
limitHy.setMaxAccess(_B)
if mibBuilder.loadTexts:limitHy.setStatus(_A)
temp_msg=NotificationType((1,3,6,1,4,1,18248,20,1,1,0,1))
temp_msg.setObjects(*((_C,_G),(_C,_H)))
if mibBuilder.loadTexts:temp_msg.setStatus('')
mibBuilder.exportSymbols(_C,**{'PositiveInteger':PositiveInteger,'papouchProjekt':papouchProjekt,'the':the,'version1':version1,'device-var':device_var,'temp-msg':temp_msg,_G:deviceName,_H:psAlarmString,'table-channel':table_channel,'channelTable':channelTable,'channelEntry':channelEntry,'inChStatus':inChStatus,'inChValue':inChValue,'inChUnits':inChUnits,'table-watchValue':table_watchValue,'watchValTable':watchValTable,'watchValEntry':watchValEntry,'modeWatch':modeWatch,'limitHi':limitHi,'limitLo':limitLo,'limitHy':limitHy})