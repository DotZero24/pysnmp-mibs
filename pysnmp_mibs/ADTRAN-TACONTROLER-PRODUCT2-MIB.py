_T='adTaCtrlEventDetails'
_S='adTaCtrlChassisSlotNumber'
_R='adTaCtrlChassisShelfNumber'
_Q='adTaCtrlProvisionClientIPAddress'
_P='adTaCtrlProvisionScmIPAddress'
_O='adTaCtrlChassisTimeStamp'
_N='adTaCtrlProvisionSnmpOIDIndex'
_M='adTaCtrlProvisionSnmpOID'
_L='adTaSysCtrlHostIndex'
_K='sysName'
_J='SNMPv2-MIB'
_I='adTrapInformSeqNum'
_H='ADTRAN-GENTRAPINFORM-MIB'
_G='disable'
_F='enable'
_E='read-only'
_D='read-write'
_C='ADTRAN-TACONTROLER-PRODUCT2-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adTrapInformSeqNum,=mibBuilder.importSymbols(_H,_I)
adTaControllerMgmt,=mibBuilder.importSymbols('ADTRAN-TACONTROLER-PRODUCT-MIB','adTaControllerMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
adTaCtrlProduct2=ModuleIdentity((1,3,6,1,4,1,664,5,63,1))
if mibBuilder.loadTexts:adTaCtrlProduct2.setRevisions(('2007-05-01 00:00',))
_AdTaSysCtrlNotifications_ObjectIdentity=ObjectIdentity
adTaSysCtrlNotifications=_AdTaSysCtrlNotifications_ObjectIdentity((1,3,6,1,4,1,664,5,63,1,0))
_AdTaSysCtrlScalars_ObjectIdentity=ObjectIdentity
adTaSysCtrlScalars=_AdTaSysCtrlScalars_ObjectIdentity((1,3,6,1,4,1,664,5,63,1,10))
class _AdTaCtrlChassisSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdTaCtrlChassisSlotNumber_Type.__name__=_B
_AdTaCtrlChassisSlotNumber_Object=MibScalar
adTaCtrlChassisSlotNumber=_AdTaCtrlChassisSlotNumber_Object((1,3,6,1,4,1,664,5,63,1,10,10),_AdTaCtrlChassisSlotNumber_Type())
adTaCtrlChassisSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:adTaCtrlChassisSlotNumber.setStatus(_A)
class _AdTaCtrlChassisShelfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdTaCtrlChassisShelfNumber_Type.__name__=_B
_AdTaCtrlChassisShelfNumber_Object=MibScalar
adTaCtrlChassisShelfNumber=_AdTaCtrlChassisShelfNumber_Object((1,3,6,1,4,1,664,5,63,1,10,11),_AdTaCtrlChassisShelfNumber_Type())
adTaCtrlChassisShelfNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:adTaCtrlChassisShelfNumber.setStatus(_A)
_AdTaCtrlChassisTimeStamp_Type=DateAndTime
_AdTaCtrlChassisTimeStamp_Object=MibScalar
adTaCtrlChassisTimeStamp=_AdTaCtrlChassisTimeStamp_Object((1,3,6,1,4,1,664,5,63,1,10,12),_AdTaCtrlChassisTimeStamp_Type())
adTaCtrlChassisTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaCtrlChassisTimeStamp.setStatus(_A)
_AdTaCtrlEventDetails_Type=OctetString
_AdTaCtrlEventDetails_Object=MibScalar
adTaCtrlEventDetails=_AdTaCtrlEventDetails_Object((1,3,6,1,4,1,664,5,63,1,10,15),_AdTaCtrlEventDetails_Type())
adTaCtrlEventDetails.setMaxAccess(_E)
if mibBuilder.loadTexts:adTaCtrlEventDetails.setStatus(_A)
_AdTaCtrlProvisionSnmpOID_Type=ObjectIdentifier
_AdTaCtrlProvisionSnmpOID_Object=MibScalar
adTaCtrlProvisionSnmpOID=_AdTaCtrlProvisionSnmpOID_Object((1,3,6,1,4,1,664,5,63,1,10,16),_AdTaCtrlProvisionSnmpOID_Type())
adTaCtrlProvisionSnmpOID.setMaxAccess(_E)
if mibBuilder.loadTexts:adTaCtrlProvisionSnmpOID.setStatus(_A)
_AdTaCtrlProvisionSnmpOIDIndex_Type=ObjectIdentifier
_AdTaCtrlProvisionSnmpOIDIndex_Object=MibScalar
adTaCtrlProvisionSnmpOIDIndex=_AdTaCtrlProvisionSnmpOIDIndex_Object((1,3,6,1,4,1,664,5,63,1,10,17),_AdTaCtrlProvisionSnmpOIDIndex_Type())
adTaCtrlProvisionSnmpOIDIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:adTaCtrlProvisionSnmpOIDIndex.setStatus(_A)
_AdTaCtrlProvisionClientIPAddress_Type=IpAddress
_AdTaCtrlProvisionClientIPAddress_Object=MibScalar
adTaCtrlProvisionClientIPAddress=_AdTaCtrlProvisionClientIPAddress_Object((1,3,6,1,4,1,664,5,63,1,10,18),_AdTaCtrlProvisionClientIPAddress_Type())
adTaCtrlProvisionClientIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:adTaCtrlProvisionClientIPAddress.setStatus(_A)
_AdTaCtrlProvisionScmIPAddress_Type=IpAddress
_AdTaCtrlProvisionScmIPAddress_Object=MibScalar
adTaCtrlProvisionScmIPAddress=_AdTaCtrlProvisionScmIPAddress_Object((1,3,6,1,4,1,664,5,63,1,10,19),_AdTaCtrlProvisionScmIPAddress_Type())
adTaCtrlProvisionScmIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:adTaCtrlProvisionScmIPAddress.setStatus(_A)
_AdTaSysCtrlSnmpProvChange_ObjectIdentity=ObjectIdentity
adTaSysCtrlSnmpProvChange=_AdTaSysCtrlSnmpProvChange_ObjectIdentity((1,3,6,1,4,1,664,5,63,1,11))
class _AdTaSysCtrlSnmpProvChgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdTaSysCtrlSnmpProvChgMode_Type.__name__=_B
_AdTaSysCtrlSnmpProvChgMode_Object=MibScalar
adTaSysCtrlSnmpProvChgMode=_AdTaSysCtrlSnmpProvChgMode_Object((1,3,6,1,4,1,664,5,63,1,11,2),_AdTaSysCtrlSnmpProvChgMode_Type())
adTaSysCtrlSnmpProvChgMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaSysCtrlSnmpProvChgMode.setStatus(_A)
class _AdTaSysCtrlSCMProvChgTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdTaSysCtrlSCMProvChgTrapMode_Type.__name__=_B
_AdTaSysCtrlSCMProvChgTrapMode_Object=MibScalar
adTaSysCtrlSCMProvChgTrapMode=_AdTaSysCtrlSCMProvChgTrapMode_Object((1,3,6,1,4,1,664,5,63,1,11,3),_AdTaSysCtrlSCMProvChgTrapMode_Type())
adTaSysCtrlSCMProvChgTrapMode.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaSysCtrlSCMProvChgTrapMode.setStatus(_A)
class _AdTaSysCtrlSnmpNotifyHost1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdTaSysCtrlSnmpNotifyHost1_Type.__name__=_B
_AdTaSysCtrlSnmpNotifyHost1_Object=MibScalar
adTaSysCtrlSnmpNotifyHost1=_AdTaSysCtrlSnmpNotifyHost1_Object((1,3,6,1,4,1,664,5,63,1,11,5),_AdTaSysCtrlSnmpNotifyHost1_Type())
adTaSysCtrlSnmpNotifyHost1.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaSysCtrlSnmpNotifyHost1.setStatus(_A)
class _AdTaSysCtrlSnmpNotifyHost2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdTaSysCtrlSnmpNotifyHost2_Type.__name__=_B
_AdTaSysCtrlSnmpNotifyHost2_Object=MibScalar
adTaSysCtrlSnmpNotifyHost2=_AdTaSysCtrlSnmpNotifyHost2_Object((1,3,6,1,4,1,664,5,63,1,11,6),_AdTaSysCtrlSnmpNotifyHost2_Type())
adTaSysCtrlSnmpNotifyHost2.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaSysCtrlSnmpNotifyHost2.setStatus(_A)
class _AdTaSysCtrlSnmpNotifyHost3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdTaSysCtrlSnmpNotifyHost3_Type.__name__=_B
_AdTaSysCtrlSnmpNotifyHost3_Object=MibScalar
adTaSysCtrlSnmpNotifyHost3=_AdTaSysCtrlSnmpNotifyHost3_Object((1,3,6,1,4,1,664,5,63,1,11,7),_AdTaSysCtrlSnmpNotifyHost3_Type())
adTaSysCtrlSnmpNotifyHost3.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaSysCtrlSnmpNotifyHost3.setStatus(_A)
class _AdTaSysCtrlSnmpNotifyHost4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AdTaSysCtrlSnmpNotifyHost4_Type.__name__=_B
_AdTaSysCtrlSnmpNotifyHost4_Object=MibScalar
adTaSysCtrlSnmpNotifyHost4=_AdTaSysCtrlSnmpNotifyHost4_Object((1,3,6,1,4,1,664,5,63,1,11,8),_AdTaSysCtrlSnmpNotifyHost4_Type())
adTaSysCtrlSnmpNotifyHost4.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaSysCtrlSnmpNotifyHost4.setStatus(_A)
_AdTaSysCtrlOriginatorHostTable_Object=MibTable
adTaSysCtrlOriginatorHostTable=_AdTaSysCtrlOriginatorHostTable_Object((1,3,6,1,4,1,664,5,63,1,11,10))
if mibBuilder.loadTexts:adTaSysCtrlOriginatorHostTable.setStatus(_A)
_AdTaSysCtrlOriginatorHostEntry_Object=MibTableRow
adTaSysCtrlOriginatorHostEntry=_AdTaSysCtrlOriginatorHostEntry_Object((1,3,6,1,4,1,664,5,63,1,11,10,1))
adTaSysCtrlOriginatorHostEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:adTaSysCtrlOriginatorHostEntry.setStatus(_A)
class _AdTaSysCtrlHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AdTaSysCtrlHostIndex_Type.__name__=_B
_AdTaSysCtrlHostIndex_Object=MibTableColumn
adTaSysCtrlHostIndex=_AdTaSysCtrlHostIndex_Object((1,3,6,1,4,1,664,5,63,1,11,10,1,1),_AdTaSysCtrlHostIndex_Type())
adTaSysCtrlHostIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adTaSysCtrlHostIndex.setStatus(_A)
_AdTaSysCtrlOriginatorHostDisable_Type=IpAddress
_AdTaSysCtrlOriginatorHostDisable_Object=MibTableColumn
adTaSysCtrlOriginatorHostDisable=_AdTaSysCtrlOriginatorHostDisable_Object((1,3,6,1,4,1,664,5,63,1,11,10,1,2),_AdTaSysCtrlOriginatorHostDisable_Type())
adTaSysCtrlOriginatorHostDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:adTaSysCtrlOriginatorHostDisable.setStatus(_A)
adTAModuleProvisionChange=NotificationType((1,3,6,1,4,1,664,5,63,1,0,2))
adTAModuleProvisionChange.setObjects(*((_H,_I),(_J,_K),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:adTAModuleProvisionChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'adTaCtrlProduct2':adTaCtrlProduct2,'adTaSysCtrlNotifications':adTaSysCtrlNotifications,'adTAModuleProvisionChange':adTAModuleProvisionChange,'adTaSysCtrlScalars':adTaSysCtrlScalars,_S:adTaCtrlChassisSlotNumber,_R:adTaCtrlChassisShelfNumber,_O:adTaCtrlChassisTimeStamp,_T:adTaCtrlEventDetails,_M:adTaCtrlProvisionSnmpOID,_N:adTaCtrlProvisionSnmpOIDIndex,_Q:adTaCtrlProvisionClientIPAddress,_P:adTaCtrlProvisionScmIPAddress,'adTaSysCtrlSnmpProvChange':adTaSysCtrlSnmpProvChange,'adTaSysCtrlSnmpProvChgMode':adTaSysCtrlSnmpProvChgMode,'adTaSysCtrlSCMProvChgTrapMode':adTaSysCtrlSCMProvChgTrapMode,'adTaSysCtrlSnmpNotifyHost1':adTaSysCtrlSnmpNotifyHost1,'adTaSysCtrlSnmpNotifyHost2':adTaSysCtrlSnmpNotifyHost2,'adTaSysCtrlSnmpNotifyHost3':adTaSysCtrlSnmpNotifyHost3,'adTaSysCtrlSnmpNotifyHost4':adTaSysCtrlSnmpNotifyHost4,'adTaSysCtrlOriginatorHostTable':adTaSysCtrlOriginatorHostTable,'adTaSysCtrlOriginatorHostEntry':adTaSysCtrlOriginatorHostEntry,_L:adTaSysCtrlHostIndex,'adTaSysCtrlOriginatorHostDisable':adTaSysCtrlOriginatorHostDisable})