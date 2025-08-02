_Q='analogindex'
_P='outputindex'
_O='sensorindex'
_N='DisplayString'
_M='inputstatus'
_L='sensortype'
_K='name'
_J='current'
_I='inputindex'
_H='Integer32'
_G='address'
_F='location'
_E='uptime'
_D='read-write'
_C='read-only'
_B='BETTER-NETWORKS-ETHERNETBOX-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Betternetworks_ObjectIdentity=ObjectIdentity
betternetworks=_Betternetworks_ObjectIdentity((1,3,6,1,4,1,14848))
_Ethernetbox_ObjectIdentity=ObjectIdentity
ethernetbox=_Ethernetbox_ObjectIdentity((1,3,6,1,4,1,14848,2))
_EthernetboxObjects_ObjectIdentity=ObjectIdentity
ethernetboxObjects=_EthernetboxObjects_ObjectIdentity((1,3,6,1,4,1,14848,2,1))
_Misc_ObjectIdentity=ObjectIdentity
misc=_Misc_ObjectIdentity((1,3,6,1,4,1,14848,2,1,1))
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,14848,2,1,1,1),_Version_Type())
version.setMaxAccess(_C)
if mibBuilder.loadTexts:version.setStatus(_A)
_Location_Type=DisplayString
_Location_Object=MibScalar
location=_Location_Object((1,3,6,1,4,1,14848,2,1,1,2),_Location_Type())
location.setMaxAccess(_D)
if mibBuilder.loadTexts:location.setStatus(_A)
class _Tempunit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Tempunit_Type.__name__=_H
_Tempunit_Object=MibScalar
tempunit=_Tempunit_Object((1,3,6,1,4,1,14848,2,1,1,3),_Tempunit_Type())
tempunit.setMaxAccess(_C)
if mibBuilder.loadTexts:tempunit.setStatus(_A)
class _Refreshinterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Refreshinterval_Type.__name__=_H
_Refreshinterval_Object=MibScalar
refreshinterval=_Refreshinterval_Object((1,3,6,1,4,1,14848,2,1,1,4),_Refreshinterval_Type())
refreshinterval.setMaxAccess(_C)
if mibBuilder.loadTexts:refreshinterval.setStatus(_A)
class _Numbersensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_Numbersensors_Type.__name__=_H
_Numbersensors_Object=MibScalar
numbersensors=_Numbersensors_Object((1,3,6,1,4,1,14848,2,1,1,5),_Numbersensors_Type())
numbersensors.setMaxAccess(_C)
if mibBuilder.loadTexts:numbersensors.setStatus(_A)
_Address_Type=IpAddress
_Address_Object=MibScalar
address=_Address_Object((1,3,6,1,4,1,14848,2,1,1,6),_Address_Type())
address.setMaxAccess(_C)
if mibBuilder.loadTexts:address.setStatus(_A)
_Uptime_Type=TimeTicks
_Uptime_Object=MibScalar
uptime=_Uptime_Object((1,3,6,1,4,1,14848,2,1,1,7),_Uptime_Type())
uptime.setMaxAccess(_C)
if mibBuilder.loadTexts:uptime.setStatus(_A)
_SensorTable_Object=MibTable
sensorTable=_SensorTable_Object((1,3,6,1,4,1,14848,2,1,2))
if mibBuilder.loadTexts:sensorTable.setStatus(_A)
_SensorEntry_Object=MibTableRow
sensorEntry=_SensorEntry_Object((1,3,6,1,4,1,14848,2,1,2,1))
sensorEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:sensorEntry.setStatus(_A)
_Sensorindex_Type=Integer32
_Sensorindex_Object=MibTableColumn
sensorindex=_Sensorindex_Object((1,3,6,1,4,1,14848,2,1,2,1,1),_Sensorindex_Type())
sensorindex.setMaxAccess(_C)
if mibBuilder.loadTexts:sensorindex.setStatus(_A)
_Name_Type=DisplayString
_Name_Object=MibTableColumn
name=_Name_Object((1,3,6,1,4,1,14848,2,1,2,1,2),_Name_Type())
name.setMaxAccess(_D)
if mibBuilder.loadTexts:name.setStatus(_A)
_Sensortype_Type=Integer32
_Sensortype_Object=MibTableColumn
sensortype=_Sensortype_Object((1,3,6,1,4,1,14848,2,1,2,1,3),_Sensortype_Type())
sensortype.setMaxAccess(_D)
if mibBuilder.loadTexts:sensortype.setStatus(_A)
_Valueint_Type=Integer32
_Valueint_Object=MibTableColumn
valueint=_Valueint_Object((1,3,6,1,4,1,14848,2,1,2,1,4),_Valueint_Type())
valueint.setMaxAccess(_C)
if mibBuilder.loadTexts:valueint.setStatus(_A)
_Valueint10_Type=Integer32
_Valueint10_Object=MibTableColumn
valueint10=_Valueint10_Object((1,3,6,1,4,1,14848,2,1,2,1,5),_Valueint10_Type())
valueint10.setMaxAccess(_C)
if mibBuilder.loadTexts:valueint10.setStatus(_A)
_Valuestr_Type=DisplayString
_Valuestr_Object=MibTableColumn
valuestr=_Valuestr_Object((1,3,6,1,4,1,14848,2,1,2,1,6),_Valuestr_Type())
valuestr.setMaxAccess(_C)
if mibBuilder.loadTexts:valuestr.setStatus(_A)
_Valid_Type=Integer32
_Valid_Object=MibTableColumn
valid=_Valid_Object((1,3,6,1,4,1,14848,2,1,2,1,7),_Valid_Type())
valid.setMaxAccess(_C)
if mibBuilder.loadTexts:valid.setStatus(_A)
_Lowlimit_Type=Integer32
_Lowlimit_Object=MibTableColumn
lowlimit=_Lowlimit_Object((1,3,6,1,4,1,14848,2,1,2,1,8),_Lowlimit_Type())
lowlimit.setMaxAccess(_D)
if mibBuilder.loadTexts:lowlimit.setStatus(_A)
_Highlimit_Type=Integer32
_Highlimit_Object=MibTableColumn
highlimit=_Highlimit_Object((1,3,6,1,4,1,14848,2,1,2,1,9),_Highlimit_Type())
highlimit.setMaxAccess(_D)
if mibBuilder.loadTexts:highlimit.setStatus(_A)
_Hysteresis_Type=Integer32
_Hysteresis_Object=MibTableColumn
hysteresis=_Hysteresis_Object((1,3,6,1,4,1,14848,2,1,2,1,10),_Hysteresis_Type())
hysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:hysteresis.setStatus(_A)
_Status_Type=Integer32
_Status_Object=MibTableColumn
status=_Status_Object((1,3,6,1,4,1,14848,2,1,2,1,11),_Status_Type())
status.setMaxAccess(_C)
if mibBuilder.loadTexts:status.setStatus(_A)
_InputTable_Object=MibTable
inputTable=_InputTable_Object((1,3,6,1,4,1,14848,2,1,3))
if mibBuilder.loadTexts:inputTable.setStatus(_A)
_InputEntry_Object=MibTableRow
inputEntry=_InputEntry_Object((1,3,6,1,4,1,14848,2,1,3,1))
inputEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:inputEntry.setStatus(_A)
_Inputindex_Type=Integer32
_Inputindex_Object=MibTableColumn
inputindex=_Inputindex_Object((1,3,6,1,4,1,14848,2,1,3,1,1),_Inputindex_Type())
inputindex.setMaxAccess(_C)
if mibBuilder.loadTexts:inputindex.setStatus(_A)
_Inputstatus_Type=Integer32
_Inputstatus_Object=MibTableColumn
inputstatus=_Inputstatus_Object((1,3,6,1,4,1,14848,2,1,3,1,2),_Inputstatus_Type())
inputstatus.setMaxAccess(_C)
if mibBuilder.loadTexts:inputstatus.setStatus(_A)
_OutputTable_Object=MibTable
outputTable=_OutputTable_Object((1,3,6,1,4,1,14848,2,1,4))
if mibBuilder.loadTexts:outputTable.setStatus(_A)
_OutputEntry_Object=MibTableRow
outputEntry=_OutputEntry_Object((1,3,6,1,4,1,14848,2,1,4,1))
outputEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:outputEntry.setStatus(_A)
_Outputindex_Type=Integer32
_Outputindex_Object=MibTableColumn
outputindex=_Outputindex_Object((1,3,6,1,4,1,14848,2,1,4,1,1),_Outputindex_Type())
outputindex.setMaxAccess(_C)
if mibBuilder.loadTexts:outputindex.setStatus(_A)
_Outputstatus_Type=Integer32
_Outputstatus_Object=MibTableColumn
outputstatus=_Outputstatus_Object((1,3,6,1,4,1,14848,2,1,4,1,2),_Outputstatus_Type())
outputstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:outputstatus.setStatus(_A)
_AnalogTable_Object=MibTable
analogTable=_AnalogTable_Object((1,3,6,1,4,1,14848,2,1,5))
if mibBuilder.loadTexts:analogTable.setStatus(_A)
_AnalogEntry_Object=MibTableRow
analogEntry=_AnalogEntry_Object((1,3,6,1,4,1,14848,2,1,5,1))
analogEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:analogEntry.setStatus(_A)
_Analogindex_Type=Integer32
_Analogindex_Object=MibTableColumn
analogindex=_Analogindex_Object((1,3,6,1,4,1,14848,2,1,5,1,1),_Analogindex_Type())
analogindex.setMaxAccess(_C)
if mibBuilder.loadTexts:analogindex.setStatus(_A)
_Analogname_Type=DisplayString
_Analogname_Object=MibTableColumn
analogname=_Analogname_Object((1,3,6,1,4,1,14848,2,1,5,1,2),_Analogname_Type())
analogname.setMaxAccess(_D)
if mibBuilder.loadTexts:analogname.setStatus(_A)
_Analogvalueint_Type=Integer32
_Analogvalueint_Object=MibTableColumn
analogvalueint=_Analogvalueint_Object((1,3,6,1,4,1,14848,2,1,5,1,3),_Analogvalueint_Type())
analogvalueint.setMaxAccess(_C)
if mibBuilder.loadTexts:analogvalueint.setStatus(_A)
_Analogvalueint10_Type=Integer32
_Analogvalueint10_Object=MibTableColumn
analogvalueint10=_Analogvalueint10_Object((1,3,6,1,4,1,14848,2,1,5,1,4),_Analogvalueint10_Type())
analogvalueint10.setMaxAccess(_C)
if mibBuilder.loadTexts:analogvalueint10.setStatus(_A)
_Analogvaluestr_Type=DisplayString
_Analogvaluestr_Object=MibTableColumn
analogvaluestr=_Analogvaluestr_Object((1,3,6,1,4,1,14848,2,1,5,1,5),_Analogvaluestr_Type())
analogvaluestr.setMaxAccess(_C)
if mibBuilder.loadTexts:analogvaluestr.setStatus(_A)
sensorstatusChangeToLow=NotificationType((1,3,6,1,4,1,14848,0,1))
if mibBuilder.loadTexts:sensorstatusChangeToLow.setStatus('')
sensorstatusChangeToNormal=NotificationType((1,3,6,1,4,1,14848,0,2))
if mibBuilder.loadTexts:sensorstatusChangeToNormal.setStatus('')
sensorstatusChangeToHigh=NotificationType((1,3,6,1,4,1,14848,0,3))
if mibBuilder.loadTexts:sensorstatusChangeToHigh.setStatus('')
inputlineChangeToLow=NotificationType((1,3,6,1,4,1,14848,0,4))
if mibBuilder.loadTexts:inputlineChangeToLow.setStatus('')
inputlineChangeToHigh=NotificationType((1,3,6,1,4,1,14848,0,5))
if mibBuilder.loadTexts:inputlineChangeToHigh.setStatus('')
ethernetboxPowerUp=NotificationType((1,3,6,1,4,1,14848,0,100))
if mibBuilder.loadTexts:ethernetboxPowerUp.setStatus('')
ethernetboxConfigSaved=NotificationType((1,3,6,1,4,1,14848,0,101))
if mibBuilder.loadTexts:ethernetboxConfigSaved.setStatus('')
ethernetboxNotificationInputLineChangeToLow=NotificationType((1,3,6,1,4,1,14848,4))
ethernetboxNotificationInputLineChangeToLow.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_I),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ethernetboxNotificationInputLineChangeToLow.setStatus(_J)
ethernetboxNotificationInputLineChangeToHigh=NotificationType((1,3,6,1,4,1,14848,5))
ethernetboxNotificationInputLineChangeToHigh.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_I),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ethernetboxNotificationInputLineChangeToHigh.setStatus(_J)
ethernetboxNotificationPowerUp=NotificationType((1,3,6,1,4,1,14848,100))
ethernetboxNotificationPowerUp.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ethernetboxNotificationPowerUp.setStatus(_J)
ethernetboxNotificationConfigSaved=NotificationType((1,3,6,1,4,1,14848,101))
ethernetboxNotificationConfigSaved.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ethernetboxNotificationConfigSaved.setStatus(_J)
mibBuilder.exportSymbols(_B,**{_N:DisplayString,'org':org,'dod':dod,'internet':internet,'private':private,'enterprises':enterprises,'betternetworks':betternetworks,'sensorstatusChangeToLow':sensorstatusChangeToLow,'sensorstatusChangeToNormal':sensorstatusChangeToNormal,'sensorstatusChangeToHigh':sensorstatusChangeToHigh,'inputlineChangeToLow':inputlineChangeToLow,'inputlineChangeToHigh':inputlineChangeToHigh,'ethernetboxPowerUp':ethernetboxPowerUp,'ethernetboxConfigSaved':ethernetboxConfigSaved,'ethernetbox':ethernetbox,'ethernetboxObjects':ethernetboxObjects,'misc':misc,'version':version,_F:location,'tempunit':tempunit,'refreshinterval':refreshinterval,'numbersensors':numbersensors,_G:address,_E:uptime,'sensorTable':sensorTable,'sensorEntry':sensorEntry,_O:sensorindex,_K:name,_L:sensortype,'valueint':valueint,'valueint10':valueint10,'valuestr':valuestr,'valid':valid,'lowlimit':lowlimit,'highlimit':highlimit,'hysteresis':hysteresis,'status':status,'inputTable':inputTable,'inputEntry':inputEntry,_I:inputindex,_M:inputstatus,'outputTable':outputTable,'outputEntry':outputEntry,_P:outputindex,'outputstatus':outputstatus,'analogTable':analogTable,'analogEntry':analogEntry,_Q:analogindex,'analogname':analogname,'analogvalueint':analogvalueint,'analogvalueint10':analogvalueint10,'analogvaluestr':analogvaluestr,'ethernetboxNotificationInputLineChangeToLow':ethernetboxNotificationInputLineChangeToLow,'ethernetboxNotificationInputLineChangeToHigh':ethernetboxNotificationInputLineChangeToHigh,'ethernetboxNotificationPowerUp':ethernetboxNotificationPowerUp,'ethernetboxNotificationConfigSaved':ethernetboxNotificationConfigSaved})