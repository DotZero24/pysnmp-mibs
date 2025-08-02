_C='OctetString'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
affirmedSnmpModuleIDs,affirmedSnmpObjects=mibBuilder.importSymbols('AFFIRMED-SNMP-MIB','affirmedSnmpModuleIDs','affirmedSnmpObjects')
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
affirmedAlarmMIB=ModuleIdentity((1,3,6,1,4,1,37963,3,1,1))
_AffirmedAlarmObjects_ObjectIdentity=ObjectIdentity
affirmedAlarmObjects=_AffirmedAlarmObjects_ObjectIdentity((1,3,6,1,4,1,37963,1,1))
_AffirmedAlarmSeqId_Type=Integer32
_AffirmedAlarmSeqId_Object=MibScalar
affirmedAlarmSeqId=_AffirmedAlarmSeqId_Object((1,3,6,1,4,1,37963,1,1,1),_AffirmedAlarmSeqId_Type())
affirmedAlarmSeqId.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedAlarmSeqId.setStatus(_B)
class _AffirmedAlarmDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AffirmedAlarmDateTime_Type.__name__=_C
_AffirmedAlarmDateTime_Object=MibScalar
affirmedAlarmDateTime=_AffirmedAlarmDateTime_Object((1,3,6,1,4,1,37963,1,1,2),_AffirmedAlarmDateTime_Type())
affirmedAlarmDateTime.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedAlarmDateTime.setStatus(_B)
class _AffirmedAlarmChassisName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_AffirmedAlarmChassisName_Type.__name__=_C
_AffirmedAlarmChassisName_Object=MibScalar
affirmedAlarmChassisName=_AffirmedAlarmChassisName_Object((1,3,6,1,4,1,37963,1,1,3),_AffirmedAlarmChassisName_Type())
affirmedAlarmChassisName.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedAlarmChassisName.setStatus(_B)
class _AffirmedAlarmSourceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AffirmedAlarmSourceId_Type.__name__=_C
_AffirmedAlarmSourceId_Object=MibScalar
affirmedAlarmSourceId=_AffirmedAlarmSourceId_Object((1,3,6,1,4,1,37963,1,1,4),_AffirmedAlarmSourceId_Type())
affirmedAlarmSourceId.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedAlarmSourceId.setStatus(_B)
_AffirmedAlarmSeverity_Type=ItuPerceivedSeverity
_AffirmedAlarmSeverity_Object=MibScalar
affirmedAlarmSeverity=_AffirmedAlarmSeverity_Object((1,3,6,1,4,1,37963,1,1,5),_AffirmedAlarmSeverity_Type())
affirmedAlarmSeverity.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedAlarmSeverity.setStatus(_B)
_AffirmedAlarmRefSeqId_Type=Integer32
_AffirmedAlarmRefSeqId_Object=MibScalar
affirmedAlarmRefSeqId=_AffirmedAlarmRefSeqId_Object((1,3,6,1,4,1,37963,1,1,6),_AffirmedAlarmRefSeqId_Type())
affirmedAlarmRefSeqId.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedAlarmRefSeqId.setStatus(_B)
class _AffirmedAlarmDetails_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AffirmedAlarmDetails_Type.__name__=_C
_AffirmedAlarmDetails_Object=MibScalar
affirmedAlarmDetails=_AffirmedAlarmDetails_Object((1,3,6,1,4,1,37963,1,1,7),_AffirmedAlarmDetails_Type())
affirmedAlarmDetails.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedAlarmDetails.setStatus(_B)
class _AffirmedPotentialImpact_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,750))
_AffirmedPotentialImpact_Type.__name__=_C
_AffirmedPotentialImpact_Object=MibScalar
affirmedPotentialImpact=_AffirmedPotentialImpact_Object((1,3,6,1,4,1,37963,1,1,8),_AffirmedPotentialImpact_Type())
affirmedPotentialImpact.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedPotentialImpact.setStatus(_B)
class _AffirmedCorrectiveAction_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,750))
_AffirmedCorrectiveAction_Type.__name__=_C
_AffirmedCorrectiveAction_Object=MibScalar
affirmedCorrectiveAction=_AffirmedCorrectiveAction_Object((1,3,6,1,4,1,37963,1,1,9),_AffirmedCorrectiveAction_Type())
affirmedCorrectiveAction.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedCorrectiveAction.setStatus(_B)
class _AffirmedVmSourceIpAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AffirmedVmSourceIpAddress_Type.__name__=_C
_AffirmedVmSourceIpAddress_Object=MibScalar
affirmedVmSourceIpAddress=_AffirmedVmSourceIpAddress_Object((1,3,6,1,4,1,37963,1,1,10),_AffirmedVmSourceIpAddress_Type())
affirmedVmSourceIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedVmSourceIpAddress.setStatus(_B)
class _AffirmedVmSourceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AffirmedVmSourceName_Type.__name__=_C
_AffirmedVmSourceName_Object=MibScalar
affirmedVmSourceName=_AffirmedVmSourceName_Object((1,3,6,1,4,1,37963,1,1,11),_AffirmedVmSourceName_Type())
affirmedVmSourceName.setMaxAccess(_A)
if mibBuilder.loadTexts:affirmedVmSourceName.setStatus(_B)
class _Name_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Name_Type.__name__=_C
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,37963,1,1,12),_Name_Type())
name.setMaxAccess(_A)
if mibBuilder.loadTexts:name.setStatus(_B)
class _Chassis_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Chassis_Type.__name__=_C
_Chassis_Object=MibScalar
chassis=_Chassis_Object((1,3,6,1,4,1,37963,1,1,13),_Chassis_Type())
chassis.setMaxAccess(_A)
if mibBuilder.loadTexts:chassis.setStatus(_B)
class _Slot_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Slot_Type.__name__=_C
_Slot_Object=MibScalar
slot=_Slot_Object((1,3,6,1,4,1,37963,1,1,14),_Slot_Type())
slot.setMaxAccess(_A)
if mibBuilder.loadTexts:slot.setStatus(_B)
class _Cpu_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cpu_Type.__name__=_C
_Cpu_Object=MibScalar
cpu=_Cpu_Object((1,3,6,1,4,1,37963,1,1,15),_Cpu_Type())
cpu.setMaxAccess(_A)
if mibBuilder.loadTexts:cpu.setStatus(_B)
class _Dirname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Dirname_Type.__name__=_C
_Dirname_Object=MibScalar
dirname=_Dirname_Object((1,3,6,1,4,1,37963,1,1,16),_Dirname_Type())
dirname.setMaxAccess(_A)
if mibBuilder.loadTexts:dirname.setStatus(_B)
class _Adminstate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Adminstate_Type.__name__=_C
_Adminstate_Object=MibScalar
adminstate=_Adminstate_Object((1,3,6,1,4,1,37963,1,1,17),_Adminstate_Type())
adminstate.setMaxAccess(_A)
if mibBuilder.loadTexts:adminstate.setStatus(_B)
class _Resource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Resource_Type.__name__=_C
_Resource_Object=MibScalar
resource=_Resource_Object((1,3,6,1,4,1,37963,1,1,18),_Resource_Type())
resource.setMaxAccess(_A)
if mibBuilder.loadTexts:resource.setStatus(_B)
class _Sensor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Sensor_Type.__name__=_C
_Sensor_Object=MibScalar
sensor=_Sensor_Object((1,3,6,1,4,1,37963,1,1,19),_Sensor_Type())
sensor.setMaxAccess(_A)
if mibBuilder.loadTexts:sensor.setStatus(_B)
class _Data_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Data_Type.__name__=_C
_Data_Object=MibScalar
data=_Data_Object((1,3,6,1,4,1,37963,1,1,20),_Data_Type())
data.setMaxAccess(_A)
if mibBuilder.loadTexts:data.setStatus(_B)
class _Taskname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Taskname_Type.__name__=_C
_Taskname_Object=MibScalar
taskname=_Taskname_Object((1,3,6,1,4,1,37963,1,1,21),_Taskname_Type())
taskname.setMaxAccess(_A)
if mibBuilder.loadTexts:taskname.setStatus(_B)
class _Cid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cid_Type.__name__=_C
_Cid_Object=MibScalar
cid=_Cid_Object((1,3,6,1,4,1,37963,1,1,22),_Cid_Type())
cid.setMaxAccess(_A)
if mibBuilder.loadTexts:cid.setStatus(_B)
class _Sid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Sid_Type.__name__=_C
_Sid_Object=MibScalar
sid=_Sid_Object((1,3,6,1,4,1,37963,1,1,23),_Sid_Type())
sid.setMaxAccess(_A)
if mibBuilder.loadTexts:sid.setStatus(_B)
class _Type_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Type_Type.__name__=_C
_Type_Object=MibScalar
type=_Type_Object((1,3,6,1,4,1,37963,1,1,24),_Type_Type())
type.setMaxAccess(_A)
if mibBuilder.loadTexts:type.setStatus(_B)
class _Subtype_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Subtype_Type.__name__=_C
_Subtype_Object=MibScalar
subtype=_Subtype_Object((1,3,6,1,4,1,37963,1,1,25),_Subtype_Type())
subtype.setMaxAccess(_A)
if mibBuilder.loadTexts:subtype.setStatus(_B)
class _Level_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Level_Type.__name__=_C
_Level_Object=MibScalar
level=_Level_Object((1,3,6,1,4,1,37963,1,1,26),_Level_Type())
level.setMaxAccess(_A)
if mibBuilder.loadTexts:level.setStatus(_B)
class _Time_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Time_Type.__name__=_C
_Time_Object=MibScalar
time=_Time_Object((1,3,6,1,4,1,37963,1,1,27),_Time_Type())
time.setMaxAccess(_A)
if mibBuilder.loadTexts:time.setStatus(_B)
class _Services_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Services_Type.__name__=_C
_Services_Object=MibScalar
services=_Services_Object((1,3,6,1,4,1,37963,1,1,28),_Services_Type())
services.setMaxAccess(_A)
if mibBuilder.loadTexts:services.setStatus(_B)
class _Actions_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Actions_Type.__name__=_C
_Actions_Object=MibScalar
actions=_Actions_Object((1,3,6,1,4,1,37963,1,1,29),_Actions_Type())
actions.setMaxAccess(_A)
if mibBuilder.loadTexts:actions.setStatus(_B)
class _Ledname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ledname_Type.__name__=_C
_Ledname_Object=MibScalar
ledname=_Ledname_Object((1,3,6,1,4,1,37963,1,1,30),_Ledname_Type())
ledname.setMaxAccess(_A)
if mibBuilder.loadTexts:ledname.setStatus(_B)
class _Ledcolor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ledcolor_Type.__name__=_C
_Ledcolor_Object=MibScalar
ledcolor=_Ledcolor_Object((1,3,6,1,4,1,37963,1,1,31),_Ledcolor_Type())
ledcolor.setMaxAccess(_A)
if mibBuilder.loadTexts:ledcolor.setStatus(_B)
class _Usid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Usid_Type.__name__=_C
_Usid_Object=MibScalar
usid=_Usid_Object((1,3,6,1,4,1,37963,1,1,32),_Usid_Type())
usid.setMaxAccess(_A)
if mibBuilder.loadTexts:usid.setStatus(_B)
class _Hardorsoft_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Hardorsoft_Type.__name__=_C
_Hardorsoft_Object=MibScalar
hardorsoft=_Hardorsoft_Object((1,3,6,1,4,1,37963,1,1,33),_Hardorsoft_Type())
hardorsoft.setMaxAccess(_A)
if mibBuilder.loadTexts:hardorsoft.setStatus(_B)
class _Readerrors_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Readerrors_Type.__name__=_C
_Readerrors_Object=MibScalar
readerrors=_Readerrors_Object((1,3,6,1,4,1,37963,1,1,34),_Readerrors_Type())
readerrors.setMaxAccess(_A)
if mibBuilder.loadTexts:readerrors.setStatus(_B)
class _Writeerrors_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Writeerrors_Type.__name__=_C
_Writeerrors_Object=MibScalar
writeerrors=_Writeerrors_Object((1,3,6,1,4,1,37963,1,1,35),_Writeerrors_Type())
writeerrors.setMaxAccess(_A)
if mibBuilder.loadTexts:writeerrors.setStatus(_B)
class _Slotnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Slotnumber_Type.__name__=_C
_Slotnumber_Object=MibScalar
slotnumber=_Slotnumber_Object((1,3,6,1,4,1,37963,1,1,36),_Slotnumber_Type())
slotnumber.setMaxAccess(_A)
if mibBuilder.loadTexts:slotnumber.setStatus(_B)
class _Failuredescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Failuredescription_Type.__name__=_C
_Failuredescription_Object=MibScalar
failuredescription=_Failuredescription_Object((1,3,6,1,4,1,37963,1,1,37),_Failuredescription_Type())
failuredescription.setMaxAccess(_A)
if mibBuilder.loadTexts:failuredescription.setStatus(_B)
class _Suggestedrecovery_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Suggestedrecovery_Type.__name__=_C
_Suggestedrecovery_Object=MibScalar
suggestedrecovery=_Suggestedrecovery_Object((1,3,6,1,4,1,37963,1,1,38),_Suggestedrecovery_Type())
suggestedrecovery.setMaxAccess(_A)
if mibBuilder.loadTexts:suggestedrecovery.setStatus(_B)
class _Netcontext_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Netcontext_Type.__name__=_C
_Netcontext_Object=MibScalar
netcontext=_Netcontext_Object((1,3,6,1,4,1,37963,1,1,39),_Netcontext_Type())
netcontext.setMaxAccess(_A)
if mibBuilder.loadTexts:netcontext.setStatus(_B)
class _Info_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Info_Type.__name__=_C
_Info_Object=MibScalar
info=_Info_Object((1,3,6,1,4,1,37963,1,1,40),_Info_Type())
info.setMaxAccess(_A)
if mibBuilder.loadTexts:info.setStatus(_B)
class _Nodename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Nodename_Type.__name__=_C
_Nodename_Object=MibScalar
nodename=_Nodename_Object((1,3,6,1,4,1,37963,1,1,41),_Nodename_Type())
nodename.setMaxAccess(_A)
if mibBuilder.loadTexts:nodename.setStatus(_B)
class _Realmname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Realmname_Type.__name__=_C
_Realmname_Object=MibScalar
realmname=_Realmname_Object((1,3,6,1,4,1,37963,1,1,42),_Realmname_Type())
realmname.setMaxAccess(_A)
if mibBuilder.loadTexts:realmname.setStatus(_B)
class _Localhostidentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Localhostidentity_Type.__name__=_C
_Localhostidentity_Object=MibScalar
localhostidentity=_Localhostidentity_Object((1,3,6,1,4,1,37963,1,1,43),_Localhostidentity_Type())
localhostidentity.setMaxAccess(_A)
if mibBuilder.loadTexts:localhostidentity.setStatus(_B)
class _Peerrealmname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Peerrealmname_Type.__name__=_C
_Peerrealmname_Object=MibScalar
peerrealmname=_Peerrealmname_Object((1,3,6,1,4,1,37963,1,1,44),_Peerrealmname_Type())
peerrealmname.setMaxAccess(_A)
if mibBuilder.loadTexts:peerrealmname.setStatus(_B)
class _Peerhostidentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Peerhostidentity_Type.__name__=_C
_Peerhostidentity_Object=MibScalar
peerhostidentity=_Peerhostidentity_Object((1,3,6,1,4,1,37963,1,1,45),_Peerhostidentity_Type())
peerhostidentity.setMaxAccess(_A)
if mibBuilder.loadTexts:peerhostidentity.setStatus(_B)
class _Peername_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Peername_Type.__name__=_C
_Peername_Object=MibScalar
peername=_Peername_Object((1,3,6,1,4,1,37963,1,1,46),_Peername_Type())
peername.setMaxAccess(_A)
if mibBuilder.loadTexts:peername.setStatus(_B)
class _Clientid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Clientid_Type.__name__=_C
_Clientid_Object=MibScalar
clientid=_Clientid_Object((1,3,6,1,4,1,37963,1,1,47),_Clientid_Type())
clientid.setMaxAccess(_A)
if mibBuilder.loadTexts:clientid.setStatus(_B)
class _Servicename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Servicename_Type.__name__=_C
_Servicename_Object=MibScalar
servicename=_Servicename_Object((1,3,6,1,4,1,37963,1,1,48),_Servicename_Type())
servicename.setMaxAccess(_A)
if mibBuilder.loadTexts:servicename.setStatus(_B)
class _Apnname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Apnname_Type.__name__=_C
_Apnname_Object=MibScalar
apnname=_Apnname_Object((1,3,6,1,4,1,37963,1,1,49),_Apnname_Type())
apnname.setMaxAccess(_A)
if mibBuilder.loadTexts:apnname.setStatus(_B)
class _Imsi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Imsi_Type.__name__=_C
_Imsi_Object=MibScalar
imsi=_Imsi_Object((1,3,6,1,4,1,37963,1,1,50),_Imsi_Type())
imsi.setMaxAccess(_A)
if mibBuilder.loadTexts:imsi.setStatus(_B)
class _Statestring_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Statestring_Type.__name__=_C
_Statestring_Object=MibScalar
statestring=_Statestring_Object((1,3,6,1,4,1,37963,1,1,51),_Statestring_Type())
statestring.setMaxAccess(_A)
if mibBuilder.loadTexts:statestring.setStatus(_B)
class _Filepath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Filepath_Type.__name__=_C
_Filepath_Object=MibScalar
filepath=_Filepath_Object((1,3,6,1,4,1,37963,1,1,52),_Filepath_Type())
filepath.setMaxAccess(_A)
if mibBuilder.loadTexts:filepath.setStatus(_B)
class _Ip_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ip_Type.__name__=_C
_Ip_Object=MibScalar
ip=_Ip_Object((1,3,6,1,4,1,37963,1,1,53),_Ip_Type())
ip.setMaxAccess(_A)
if mibBuilder.loadTexts:ip.setStatus(_B)
class _Port_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Port_Type.__name__=_C
_Port_Object=MibScalar
port=_Port_Object((1,3,6,1,4,1,37963,1,1,54),_Port_Type())
port.setMaxAccess(_A)
if mibBuilder.loadTexts:port.setStatus(_B)
class _Chassisid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Chassisid_Type.__name__=_C
_Chassisid_Object=MibScalar
chassisid=_Chassisid_Object((1,3,6,1,4,1,37963,1,1,55),_Chassisid_Type())
chassisid.setMaxAccess(_A)
if mibBuilder.loadTexts:chassisid.setStatus(_B)
class _Slotid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Slotid_Type.__name__=_C
_Slotid_Object=MibScalar
slotid=_Slotid_Object((1,3,6,1,4,1,37963,1,1,56),_Slotid_Type())
slotid.setMaxAccess(_A)
if mibBuilder.loadTexts:slotid.setStatus(_B)
class _Cpuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cpuid_Type.__name__=_C
_Cpuid_Object=MibScalar
cpuid=_Cpuid_Object((1,3,6,1,4,1,37963,1,1,57),_Cpuid_Type())
cpuid.setMaxAccess(_A)
if mibBuilder.loadTexts:cpuid.setStatus(_B)
class _Prefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Prefix_Type.__name__=_C
_Prefix_Object=MibScalar
prefix=_Prefix_Object((1,3,6,1,4,1,37963,1,1,58),_Prefix_Type())
prefix.setMaxAccess(_A)
if mibBuilder.loadTexts:prefix.setStatus(_B)
class _Numpurged_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Numpurged_Type.__name__=_C
_Numpurged_Object=MibScalar
numpurged=_Numpurged_Object((1,3,6,1,4,1,37963,1,1,59),_Numpurged_Type())
numpurged.setMaxAccess(_A)
if mibBuilder.loadTexts:numpurged.setStatus(_B)
class _Node_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Node_Type.__name__=_C
_Node_Object=MibScalar
node=_Node_Object((1,3,6,1,4,1,37963,1,1,60),_Node_Type())
node.setMaxAccess(_A)
if mibBuilder.loadTexts:node.setStatus(_B)
class _Diskid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Diskid_Type.__name__=_C
_Diskid_Object=MibScalar
diskid=_Diskid_Object((1,3,6,1,4,1,37963,1,1,61),_Diskid_Type())
diskid.setMaxAccess(_A)
if mibBuilder.loadTexts:diskid.setStatus(_B)
class _Interfacename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Interfacename_Type.__name__=_C
_Interfacename_Object=MibScalar
interfacename=_Interfacename_Object((1,3,6,1,4,1,37963,1,1,62),_Interfacename_Type())
interfacename.setMaxAccess(_A)
if mibBuilder.loadTexts:interfacename.setStatus(_B)
class _Threshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Threshold_Type.__name__=_C
_Threshold_Object=MibScalar
threshold=_Threshold_Object((1,3,6,1,4,1,37963,1,1,63),_Threshold_Type())
threshold.setMaxAccess(_A)
if mibBuilder.loadTexts:threshold.setStatus(_B)
class _Uepoolutilization_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Uepoolutilization_Type.__name__=_C
_Uepoolutilization_Object=MibScalar
uepoolutilization=_Uepoolutilization_Object((1,3,6,1,4,1,37963,1,1,64),_Uepoolutilization_Type())
uepoolutilization.setMaxAccess(_A)
if mibBuilder.loadTexts:uepoolutilization.setStatus(_B)
class _Ipversiontype_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ipversiontype_Type.__name__=_C
_Ipversiontype_Object=MibScalar
ipversiontype=_Ipversiontype_Object((1,3,6,1,4,1,37963,1,1,65),_Ipversiontype_Type())
ipversiontype.setMaxAccess(_A)
if mibBuilder.loadTexts:ipversiontype.setStatus(_B)
class _Ifindex_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ifindex_Type.__name__=_C
_Ifindex_Object=MibScalar
ifindex=_Ifindex_Object((1,3,6,1,4,1,37963,1,1,66),_Ifindex_Type())
ifindex.setMaxAccess(_A)
if mibBuilder.loadTexts:ifindex.setStatus(_B)
class _Ifadminstatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ifadminstatus_Type.__name__=_C
_Ifadminstatus_Object=MibScalar
ifadminstatus=_Ifadminstatus_Object((1,3,6,1,4,1,37963,1,1,67),_Ifadminstatus_Type())
ifadminstatus.setMaxAccess(_A)
if mibBuilder.loadTexts:ifadminstatus.setStatus(_B)
class _Ifoperstatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ifoperstatus_Type.__name__=_C
_Ifoperstatus_Object=MibScalar
ifoperstatus=_Ifoperstatus_Object((1,3,6,1,4,1,37963,1,1,68),_Ifoperstatus_Type())
ifoperstatus.setMaxAccess(_A)
if mibBuilder.loadTexts:ifoperstatus.setStatus(_B)
class _Netctxtname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Netctxtname_Type.__name__=_C
_Netctxtname_Object=MibScalar
netctxtname=_Netctxtname_Object((1,3,6,1,4,1,37963,1,1,69),_Netctxtname_Type())
netctxtname.setMaxAccess(_A)
if mibBuilder.loadTexts:netctxtname.setStatus(_B)
class _Peeringname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Peeringname_Type.__name__=_C
_Peeringname_Object=MibScalar
peeringname=_Peeringname_Object((1,3,6,1,4,1,37963,1,1,70),_Peeringname_Type())
peeringname.setMaxAccess(_A)
if mibBuilder.loadTexts:peeringname.setStatus(_B)
class _Localpeeripaddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Localpeeripaddr_Type.__name__=_C
_Localpeeripaddr_Object=MibScalar
localpeeripaddr=_Localpeeripaddr_Object((1,3,6,1,4,1,37963,1,1,71),_Localpeeripaddr_Type())
localpeeripaddr.setMaxAccess(_A)
if mibBuilder.loadTexts:localpeeripaddr.setStatus(_B)
class _Remotepeeripaddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Remotepeeripaddr_Type.__name__=_C
_Remotepeeripaddr_Object=MibScalar
remotepeeripaddr=_Remotepeeripaddr_Object((1,3,6,1,4,1,37963,1,1,72),_Remotepeeripaddr_Type())
remotepeeripaddr.setMaxAccess(_A)
if mibBuilder.loadTexts:remotepeeripaddr.setStatus(_B)
class _Lasterrorcode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Lasterrorcode_Type.__name__=_C
_Lasterrorcode_Object=MibScalar
lasterrorcode=_Lasterrorcode_Object((1,3,6,1,4,1,37963,1,1,73),_Lasterrorcode_Type())
lasterrorcode.setMaxAccess(_A)
if mibBuilder.loadTexts:lasterrorcode.setStatus(_B)
class _Lasterrosubcode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Lasterrosubcode_Type.__name__=_C
_Lasterrosubcode_Object=MibScalar
lasterrosubcode=_Lasterrosubcode_Object((1,3,6,1,4,1,37963,1,1,74),_Lasterrosubcode_Type())
lasterrosubcode.setMaxAccess(_A)
if mibBuilder.loadTexts:lasterrosubcode.setStatus(_B)
class _Currentstate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Currentstate_Type.__name__=_C
_Currentstate_Object=MibScalar
currentstate=_Currentstate_Object((1,3,6,1,4,1,37963,1,1,75),_Currentstate_Type())
currentstate.setMaxAccess(_A)
if mibBuilder.loadTexts:currentstate.setStatus(_B)
class _Role_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Role_Type.__name__=_C
_Role_Object=MibScalar
role=_Role_Object((1,3,6,1,4,1,37963,1,1,76),_Role_Type())
role.setMaxAccess(_A)
if mibBuilder.loadTexts:role.setStatus(_B)
class _Groupname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Groupname_Type.__name__=_C
_Groupname_Object=MibScalar
groupname=_Groupname_Object((1,3,6,1,4,1,37963,1,1,77),_Groupname_Type())
groupname.setMaxAccess(_A)
if mibBuilder.loadTexts:groupname.setStatus(_B)
class _Operation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Operation_Type.__name__=_C
_Operation_Object=MibScalar
operation=_Operation_Object((1,3,6,1,4,1,37963,1,1,78),_Operation_Type())
operation.setMaxAccess(_A)
if mibBuilder.loadTexts:operation.setStatus(_B)
class _State_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_State_Type.__name__=_C
_State_Object=MibScalar
state=_State_Object((1,3,6,1,4,1,37963,1,1,79),_State_Type())
state.setMaxAccess(_A)
if mibBuilder.loadTexts:state.setStatus(_B)
class _Status_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Status_Type.__name__=_C
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,37963,1,1,80),_Status_Type())
status.setMaxAccess(_A)
if mibBuilder.loadTexts:status.setStatus(_B)
class _Activesize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Activesize_Type.__name__=_C
_Activesize_Object=MibScalar
activesize=_Activesize_Object((1,3,6,1,4,1,37963,1,1,81),_Activesize_Type())
activesize.setMaxAccess(_A)
if mibBuilder.loadTexts:activesize.setStatus(_B)
class _Standbysize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Standbysize_Type.__name__=_C
_Standbysize_Object=MibScalar
standbysize=_Standbysize_Object((1,3,6,1,4,1,37963,1,1,82),_Standbysize_Type())
standbysize.setMaxAccess(_A)
if mibBuilder.loadTexts:standbysize.setStatus(_B)
class _Mcmslotnumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Mcmslotnumber_Type.__name__=_C
_Mcmslotnumber_Object=MibScalar
mcmslotnumber=_Mcmslotnumber_Object((1,3,6,1,4,1,37963,1,1,83),_Mcmslotnumber_Type())
mcmslotnumber.setMaxAccess(_A)
if mibBuilder.loadTexts:mcmslotnumber.setStatus(_B)
class _Requiredsize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Requiredsize_Type.__name__=_C
_Requiredsize_Object=MibScalar
requiredsize=_Requiredsize_Object((1,3,6,1,4,1,37963,1,1,84),_Requiredsize_Type())
requiredsize.setMaxAccess(_A)
if mibBuilder.loadTexts:requiredsize.setStatus(_B)
class _Availablesize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Availablesize_Type.__name__=_C
_Availablesize_Object=MibScalar
availablesize=_Availablesize_Object((1,3,6,1,4,1,37963,1,1,85),_Availablesize_Type())
availablesize.setMaxAccess(_A)
if mibBuilder.loadTexts:availablesize.setStatus(_B)
class _Reason_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Reason_Type.__name__=_C
_Reason_Object=MibScalar
reason=_Reason_Object((1,3,6,1,4,1,37963,1,1,86),_Reason_Type())
reason.setMaxAccess(_A)
if mibBuilder.loadTexts:reason.setStatus(_B)
class _Importnum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Importnum_Type.__name__=_C
_Importnum_Object=MibScalar
importnum=_Importnum_Object((1,3,6,1,4,1,37963,1,1,87),_Importnum_Type())
importnum.setMaxAccess(_A)
if mibBuilder.loadTexts:importnum.setStatus(_B)
class _Resultstr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Resultstr_Type.__name__=_C
_Resultstr_Object=MibScalar
resultstr=_Resultstr_Object((1,3,6,1,4,1,37963,1,1,88),_Resultstr_Type())
resultstr.setMaxAccess(_A)
if mibBuilder.loadTexts:resultstr.setStatus(_B)
class _Datetime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Datetime_Type.__name__=_C
_Datetime_Object=MibScalar
datetime=_Datetime_Object((1,3,6,1,4,1,37963,1,1,89),_Datetime_Type())
datetime.setMaxAccess(_A)
if mibBuilder.loadTexts:datetime.setStatus(_B)
class _Fault_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Fault_Type.__name__=_C
_Fault_Object=MibScalar
fault=_Fault_Object((1,3,6,1,4,1,37963,1,1,90),_Fault_Type())
fault.setMaxAccess(_A)
if mibBuilder.loadTexts:fault.setStatus(_B)
class _Action_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Action_Type.__name__=_C
_Action_Object=MibScalar
action=_Action_Object((1,3,6,1,4,1,37963,1,1,91),_Action_Type())
action.setMaxAccess(_A)
if mibBuilder.loadTexts:action.setStatus(_B)
class _Unused_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Unused_Type.__name__=_C
_Unused_Object=MibScalar
unused=_Unused_Object((1,3,6,1,4,1,37963,1,1,92),_Unused_Type())
unused.setMaxAccess(_A)
if mibBuilder.loadTexts:unused.setStatus(_B)
class _Clusterid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Clusterid_Type.__name__=_C
_Clusterid_Object=MibScalar
clusterid=_Clusterid_Object((1,3,6,1,4,1,37963,1,1,93),_Clusterid_Type())
clusterid.setMaxAccess(_A)
if mibBuilder.loadTexts:clusterid.setStatus(_B)
class _Nodeid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Nodeid_Type.__name__=_C
_Nodeid_Object=MibScalar
nodeid=_Nodeid_Object((1,3,6,1,4,1,37963,1,1,94),_Nodeid_Type())
nodeid.setMaxAccess(_A)
if mibBuilder.loadTexts:nodeid.setStatus(_B)
class _Subsgroupname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Subsgroupname_Type.__name__=_C
_Subsgroupname_Object=MibScalar
subsgroupname=_Subsgroupname_Object((1,3,6,1,4,1,37963,1,1,95),_Subsgroupname_Type())
subsgroupname.setMaxAccess(_A)
if mibBuilder.loadTexts:subsgroupname.setStatus(_B)
class _Subsidfilename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Subsidfilename_Type.__name__=_C
_Subsidfilename_Object=MibScalar
subsidfilename=_Subsidfilename_Object((1,3,6,1,4,1,37963,1,1,96),_Subsidfilename_Type())
subsidfilename.setMaxAccess(_A)
if mibBuilder.loadTexts:subsidfilename.setStatus(_B)
class _Alarmid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Alarmid_Type.__name__=_C
_Alarmid_Object=MibScalar
alarmid=_Alarmid_Object((1,3,6,1,4,1,37963,1,1,97),_Alarmid_Type())
alarmid.setMaxAccess(_A)
if mibBuilder.loadTexts:alarmid.setStatus(_B)
class _Xpath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Xpath_Type.__name__=_C
_Xpath_Object=MibScalar
xpath=_Xpath_Object((1,3,6,1,4,1,37963,1,1,98),_Xpath_Type())
xpath.setMaxAccess(_A)
if mibBuilder.loadTexts:xpath.setStatus(_B)
class _Ifname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ifname_Type.__name__=_C
_Ifname_Object=MibScalar
ifname=_Ifname_Object((1,3,6,1,4,1,37963,1,1,99),_Ifname_Type())
ifname.setMaxAccess(_A)
if mibBuilder.loadTexts:ifname.setStatus(_B)
class _Sessionthreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Sessionthreshold_Type.__name__=_C
_Sessionthreshold_Object=MibScalar
sessionthreshold=_Sessionthreshold_Object((1,3,6,1,4,1,37963,1,1,100),_Sessionthreshold_Type())
sessionthreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:sessionthreshold.setStatus(_B)
class _Sessionutilization_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Sessionutilization_Type.__name__=_C
_Sessionutilization_Object=MibScalar
sessionutilization=_Sessionutilization_Object((1,3,6,1,4,1,37963,1,1,101),_Sessionutilization_Type())
sessionutilization.setMaxAccess(_A)
if mibBuilder.loadTexts:sessionutilization.setStatus(_B)
class _Ipaddressthreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ipaddressthreshold_Type.__name__=_C
_Ipaddressthreshold_Object=MibScalar
ipaddressthreshold=_Ipaddressthreshold_Object((1,3,6,1,4,1,37963,1,1,102),_Ipaddressthreshold_Type())
ipaddressthreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:ipaddressthreshold.setStatus(_B)
class _Ipaddressutilization_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Ipaddressutilization_Type.__name__=_C
_Ipaddressutilization_Object=MibScalar
ipaddressutilization=_Ipaddressutilization_Object((1,3,6,1,4,1,37963,1,1,103),_Ipaddressutilization_Type())
ipaddressutilization.setMaxAccess(_A)
if mibBuilder.loadTexts:ipaddressutilization.setStatus(_B)
class _Portchunkthreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Portchunkthreshold_Type.__name__=_C
_Portchunkthreshold_Object=MibScalar
portchunkthreshold=_Portchunkthreshold_Object((1,3,6,1,4,1,37963,1,1,104),_Portchunkthreshold_Type())
portchunkthreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:portchunkthreshold.setStatus(_B)
class _Portchunkutilization_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Portchunkutilization_Type.__name__=_C
_Portchunkutilization_Object=MibScalar
portchunkutilization=_Portchunkutilization_Object((1,3,6,1,4,1,37963,1,1,105),_Portchunkutilization_Type())
portchunkutilization.setMaxAccess(_A)
if mibBuilder.loadTexts:portchunkutilization.setStatus(_B)
class _Parent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Parent_Type.__name__=_C
_Parent_Object=MibScalar
parent=_Parent_Object((1,3,6,1,4,1,37963,1,1,106),_Parent_Type())
parent.setMaxAccess(_A)
if mibBuilder.loadTexts:parent.setStatus(_B)
class _Destination_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Destination_Type.__name__=_C
_Destination_Object=MibScalar
destination=_Destination_Object((1,3,6,1,4,1,37963,1,1,107),_Destination_Type())
destination.setMaxAccess(_A)
if mibBuilder.loadTexts:destination.setStatus(_B)
class _Peeripaddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Peeripaddress_Type.__name__=_C
_Peeripaddress_Object=MibScalar
peeripaddress=_Peeripaddress_Object((1,3,6,1,4,1,37963,1,1,108),_Peeripaddress_Type())
peeripaddress.setMaxAccess(_A)
if mibBuilder.loadTexts:peeripaddress.setStatus(_B)
class _Gatewayname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Gatewayname_Type.__name__=_C
_Gatewayname_Object=MibScalar
gatewayname=_Gatewayname_Object((1,3,6,1,4,1,37963,1,1,109),_Gatewayname_Type())
gatewayname.setMaxAccess(_A)
if mibBuilder.loadTexts:gatewayname.setStatus(_B)
class _Gatewayipaddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Gatewayipaddress_Type.__name__=_C
_Gatewayipaddress_Object=MibScalar
gatewayipaddress=_Gatewayipaddress_Object((1,3,6,1,4,1,37963,1,1,110),_Gatewayipaddress_Type())
gatewayipaddress.setMaxAccess(_A)
if mibBuilder.loadTexts:gatewayipaddress.setStatus(_B)
class _Bfdsessiondescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Bfdsessiondescription_Type.__name__=_C
_Bfdsessiondescription_Object=MibScalar
bfdsessiondescription=_Bfdsessiondescription_Object((1,3,6,1,4,1,37963,1,1,111),_Bfdsessiondescription_Type())
bfdsessiondescription.setMaxAccess(_A)
if mibBuilder.loadTexts:bfdsessiondescription.setStatus(_B)
class _Cafilename_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Cafilename_Type.__name__=_C
_Cafilename_Object=MibScalar
cafilename=_Cafilename_Object((1,3,6,1,4,1,37963,1,1,112),_Cafilename_Type())
cafilename.setMaxAccess(_A)
if mibBuilder.loadTexts:cafilename.setStatus(_B)
class _Expirydate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Expirydate_Type.__name__=_C
_Expirydate_Object=MibScalar
expirydate=_Expirydate_Object((1,3,6,1,4,1,37963,1,1,113),_Expirydate_Type())
expirydate.setMaxAccess(_A)
if mibBuilder.loadTexts:expirydate.setStatus(_B)
class _Index_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_Index_Type.__name__=_C
_Index_Object=MibScalar
index=_Index_Object((1,3,6,1,4,1,37963,1,1,114),_Index_Type())
index.setMaxAccess(_A)
if mibBuilder.loadTexts:index.setStatus(_B)
mibBuilder.exportSymbols('AFFIRMED-ALARM-MIB',**{'affirmedAlarmObjects':affirmedAlarmObjects,'affirmedAlarmSeqId':affirmedAlarmSeqId,'affirmedAlarmDateTime':affirmedAlarmDateTime,'affirmedAlarmChassisName':affirmedAlarmChassisName,'affirmedAlarmSourceId':affirmedAlarmSourceId,'affirmedAlarmSeverity':affirmedAlarmSeverity,'affirmedAlarmRefSeqId':affirmedAlarmRefSeqId,'affirmedAlarmDetails':affirmedAlarmDetails,'affirmedPotentialImpact':affirmedPotentialImpact,'affirmedCorrectiveAction':affirmedCorrectiveAction,'affirmedVmSourceIpAddress':affirmedVmSourceIpAddress,'affirmedVmSourceName':affirmedVmSourceName,'name':name,'chassis':chassis,'slot':slot,'cpu':cpu,'dirname':dirname,'adminstate':adminstate,'resource':resource,'sensor':sensor,'data':data,'taskname':taskname,'cid':cid,'sid':sid,'type':type,'subtype':subtype,'level':level,'time':time,'services':services,'actions':actions,'ledname':ledname,'ledcolor':ledcolor,'usid':usid,'hardorsoft':hardorsoft,'readerrors':readerrors,'writeerrors':writeerrors,'slotnumber':slotnumber,'failuredescription':failuredescription,'suggestedrecovery':suggestedrecovery,'netcontext':netcontext,'info':info,'nodename':nodename,'realmname':realmname,'localhostidentity':localhostidentity,'peerrealmname':peerrealmname,'peerhostidentity':peerhostidentity,'peername':peername,'clientid':clientid,'servicename':servicename,'apnname':apnname,'imsi':imsi,'statestring':statestring,'filepath':filepath,'ip':ip,'port':port,'chassisid':chassisid,'slotid':slotid,'cpuid':cpuid,'prefix':prefix,'numpurged':numpurged,'node':node,'diskid':diskid,'interfacename':interfacename,'threshold':threshold,'uepoolutilization':uepoolutilization,'ipversiontype':ipversiontype,'ifindex':ifindex,'ifadminstatus':ifadminstatus,'ifoperstatus':ifoperstatus,'netctxtname':netctxtname,'peeringname':peeringname,'localpeeripaddr':localpeeripaddr,'remotepeeripaddr':remotepeeripaddr,'lasterrorcode':lasterrorcode,'lasterrosubcode':lasterrosubcode,'currentstate':currentstate,'role':role,'groupname':groupname,'operation':operation,'state':state,'status':status,'activesize':activesize,'standbysize':standbysize,'mcmslotnumber':mcmslotnumber,'requiredsize':requiredsize,'availablesize':availablesize,'reason':reason,'importnum':importnum,'resultstr':resultstr,'datetime':datetime,'fault':fault,'action':action,'unused':unused,'clusterid':clusterid,'nodeid':nodeid,'subsgroupname':subsgroupname,'subsidfilename':subsidfilename,'alarmid':alarmid,'xpath':xpath,'ifname':ifname,'sessionthreshold':sessionthreshold,'sessionutilization':sessionutilization,'ipaddressthreshold':ipaddressthreshold,'ipaddressutilization':ipaddressutilization,'portchunkthreshold':portchunkthreshold,'portchunkutilization':portchunkutilization,'parent':parent,'destination':destination,'peeripaddress':peeripaddress,'gatewayname':gatewayname,'gatewayipaddress':gatewayipaddress,'bfdsessiondescription':bfdsessiondescription,'cafilename':cafilename,'expirydate':expirydate,'index':index,'affirmedAlarmMIB':affirmedAlarmMIB})