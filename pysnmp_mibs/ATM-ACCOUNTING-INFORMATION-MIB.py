_D='OctetString'
_C='Integer32'
_B='not-accessible'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmAddr,=mibBuilder.importSymbols('ATM-TC-MIB','AtmAddr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
atmAccountingInformationMIB=ModuleIdentity((1,3,6,1,2,1,59))
_AtmAcctngMIBObjects_ObjectIdentity=ObjectIdentity
atmAcctngMIBObjects=_AtmAcctngMIBObjects_ObjectIdentity((1,3,6,1,2,1,59,1))
_AtmAcctngDataObjects_ObjectIdentity=ObjectIdentity
atmAcctngDataObjects=_AtmAcctngDataObjects_ObjectIdentity((1,3,6,1,2,1,59,1,1))
if mibBuilder.loadTexts:atmAcctngDataObjects.setStatus(_A)
class _AtmAcctngConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('pvc',1),('pvp',2),('svcIncoming',3),('svcOutgoing',4),('svpIncoming',5),('svpOutgoing',6),('spvcInitiator',7),('spvcTarget',8),('spvpInitiator',9),('spvpTarget',10)))
_AtmAcctngConnectionType_Type.__name__=_C
_AtmAcctngConnectionType_Object=MibScalar
atmAcctngConnectionType=_AtmAcctngConnectionType_Object((1,3,6,1,2,1,59,1,1,1),_AtmAcctngConnectionType_Type())
atmAcctngConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngConnectionType.setStatus(_A)
class _AtmAcctngCastType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('p2p',1),('p2mp',2)))
_AtmAcctngCastType_Type.__name__=_C
_AtmAcctngCastType_Object=MibScalar
atmAcctngCastType=_AtmAcctngCastType_Object((1,3,6,1,2,1,59,1,1,2),_AtmAcctngCastType_Type())
atmAcctngCastType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCastType.setStatus(_A)
_AtmAcctngIfName_Type=DisplayString
_AtmAcctngIfName_Object=MibScalar
atmAcctngIfName=_AtmAcctngIfName_Object((1,3,6,1,2,1,59,1,1,3),_AtmAcctngIfName_Type())
atmAcctngIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngIfName.setStatus(_A)
_AtmAcctngIfAlias_Type=DisplayString
_AtmAcctngIfAlias_Object=MibScalar
atmAcctngIfAlias=_AtmAcctngIfAlias_Object((1,3,6,1,2,1,59,1,1,4),_AtmAcctngIfAlias_Type())
atmAcctngIfAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngIfAlias.setStatus(_A)
class _AtmAcctngVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AtmAcctngVpi_Type.__name__=_C
_AtmAcctngVpi_Object=MibScalar
atmAcctngVpi=_AtmAcctngVpi_Object((1,3,6,1,2,1,59,1,1,5),_AtmAcctngVpi_Type())
atmAcctngVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngVpi.setStatus(_A)
class _AtmAcctngVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmAcctngVci_Type.__name__=_C
_AtmAcctngVci_Object=MibScalar
atmAcctngVci=_AtmAcctngVci_Object((1,3,6,1,2,1,59,1,1,6),_AtmAcctngVci_Type())
atmAcctngVci.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngVci.setStatus(_A)
_AtmAcctngCallingParty_Type=AtmAddr
_AtmAcctngCallingParty_Object=MibScalar
atmAcctngCallingParty=_AtmAcctngCallingParty_Object((1,3,6,1,2,1,59,1,1,7),_AtmAcctngCallingParty_Type())
atmAcctngCallingParty.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCallingParty.setStatus(_A)
_AtmAcctngCalledParty_Type=AtmAddr
_AtmAcctngCalledParty_Object=MibScalar
atmAcctngCalledParty=_AtmAcctngCalledParty_Object((1,3,6,1,2,1,59,1,1,8),_AtmAcctngCalledParty_Type())
atmAcctngCalledParty.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCalledParty.setStatus(_A)
class _AtmAcctngCallReference_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_AtmAcctngCallReference_Type.__name__=_D
_AtmAcctngCallReference_Object=MibScalar
atmAcctngCallReference=_AtmAcctngCallReference_Object((1,3,6,1,2,1,59,1,1,9),_AtmAcctngCallReference_Type())
atmAcctngCallReference.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCallReference.setStatus(_A)
_AtmAcctngStartTime_Type=DateAndTime
_AtmAcctngStartTime_Object=MibScalar
atmAcctngStartTime=_AtmAcctngStartTime_Object((1,3,6,1,2,1,59,1,1,10),_AtmAcctngStartTime_Type())
atmAcctngStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngStartTime.setStatus(_A)
_AtmAcctngCollectionTime_Type=DateAndTime
_AtmAcctngCollectionTime_Object=MibScalar
atmAcctngCollectionTime=_AtmAcctngCollectionTime_Object((1,3,6,1,2,1,59,1,1,11),_AtmAcctngCollectionTime_Type())
atmAcctngCollectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCollectionTime.setStatus(_A)
class _AtmAcctngCollectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('onRelease',1),('periodically',2),('onCommand',3)))
_AtmAcctngCollectMode_Type.__name__=_C
_AtmAcctngCollectMode_Object=MibScalar
atmAcctngCollectMode=_AtmAcctngCollectMode_Object((1,3,6,1,2,1,59,1,1,12),_AtmAcctngCollectMode_Type())
atmAcctngCollectMode.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCollectMode.setStatus(_A)
_AtmAcctngReleaseCause_Type=Integer32
_AtmAcctngReleaseCause_Object=MibScalar
atmAcctngReleaseCause=_AtmAcctngReleaseCause_Object((1,3,6,1,2,1,59,1,1,13),_AtmAcctngReleaseCause_Type())
atmAcctngReleaseCause.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReleaseCause.setStatus(_A)
class _AtmAcctngServiceCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('cbr',2),('vbrRt',3),('vbrNrt',4),('abr',5),('ubr',6),('unknown',7)))
_AtmAcctngServiceCategory_Type.__name__=_C
_AtmAcctngServiceCategory_Object=MibScalar
atmAcctngServiceCategory=_AtmAcctngServiceCategory_Object((1,3,6,1,2,1,59,1,1,14),_AtmAcctngServiceCategory_Type())
atmAcctngServiceCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngServiceCategory.setStatus(_A)
_AtmAcctngTransmittedCells_Type=Counter64
_AtmAcctngTransmittedCells_Object=MibScalar
atmAcctngTransmittedCells=_AtmAcctngTransmittedCells_Object((1,3,6,1,2,1,59,1,1,15),_AtmAcctngTransmittedCells_Type())
atmAcctngTransmittedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmittedCells.setStatus(_A)
_AtmAcctngTransmittedClp0Cells_Type=Counter64
_AtmAcctngTransmittedClp0Cells_Object=MibScalar
atmAcctngTransmittedClp0Cells=_AtmAcctngTransmittedClp0Cells_Object((1,3,6,1,2,1,59,1,1,16),_AtmAcctngTransmittedClp0Cells_Type())
atmAcctngTransmittedClp0Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmittedClp0Cells.setStatus(_A)
_AtmAcctngReceivedCells_Type=Counter64
_AtmAcctngReceivedCells_Object=MibScalar
atmAcctngReceivedCells=_AtmAcctngReceivedCells_Object((1,3,6,1,2,1,59,1,1,17),_AtmAcctngReceivedCells_Type())
atmAcctngReceivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceivedCells.setStatus(_A)
_AtmAcctngReceivedClp0Cells_Type=Counter64
_AtmAcctngReceivedClp0Cells_Object=MibScalar
atmAcctngReceivedClp0Cells=_AtmAcctngReceivedClp0Cells_Object((1,3,6,1,2,1,59,1,1,18),_AtmAcctngReceivedClp0Cells_Type())
atmAcctngReceivedClp0Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceivedClp0Cells.setStatus(_A)
_AtmAcctngTransmitTrafficDescriptorType_Type=ObjectIdentifier
_AtmAcctngTransmitTrafficDescriptorType_Object=MibScalar
atmAcctngTransmitTrafficDescriptorType=_AtmAcctngTransmitTrafficDescriptorType_Object((1,3,6,1,2,1,59,1,1,19),_AtmAcctngTransmitTrafficDescriptorType_Type())
atmAcctngTransmitTrafficDescriptorType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmitTrafficDescriptorType.setStatus(_A)
class _AtmAcctngTransmitTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngTransmitTrafficDescriptorParam1_Type.__name__=_C
_AtmAcctngTransmitTrafficDescriptorParam1_Object=MibScalar
atmAcctngTransmitTrafficDescriptorParam1=_AtmAcctngTransmitTrafficDescriptorParam1_Object((1,3,6,1,2,1,59,1,1,20),_AtmAcctngTransmitTrafficDescriptorParam1_Type())
atmAcctngTransmitTrafficDescriptorParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmitTrafficDescriptorParam1.setStatus(_A)
class _AtmAcctngTransmitTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngTransmitTrafficDescriptorParam2_Type.__name__=_C
_AtmAcctngTransmitTrafficDescriptorParam2_Object=MibScalar
atmAcctngTransmitTrafficDescriptorParam2=_AtmAcctngTransmitTrafficDescriptorParam2_Object((1,3,6,1,2,1,59,1,1,21),_AtmAcctngTransmitTrafficDescriptorParam2_Type())
atmAcctngTransmitTrafficDescriptorParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmitTrafficDescriptorParam2.setStatus(_A)
class _AtmAcctngTransmitTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngTransmitTrafficDescriptorParam3_Type.__name__=_C
_AtmAcctngTransmitTrafficDescriptorParam3_Object=MibScalar
atmAcctngTransmitTrafficDescriptorParam3=_AtmAcctngTransmitTrafficDescriptorParam3_Object((1,3,6,1,2,1,59,1,1,22),_AtmAcctngTransmitTrafficDescriptorParam3_Type())
atmAcctngTransmitTrafficDescriptorParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmitTrafficDescriptorParam3.setStatus(_A)
class _AtmAcctngTransmitTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngTransmitTrafficDescriptorParam4_Type.__name__=_C
_AtmAcctngTransmitTrafficDescriptorParam4_Object=MibScalar
atmAcctngTransmitTrafficDescriptorParam4=_AtmAcctngTransmitTrafficDescriptorParam4_Object((1,3,6,1,2,1,59,1,1,23),_AtmAcctngTransmitTrafficDescriptorParam4_Type())
atmAcctngTransmitTrafficDescriptorParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmitTrafficDescriptorParam4.setStatus(_A)
class _AtmAcctngTransmitTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngTransmitTrafficDescriptorParam5_Type.__name__=_C
_AtmAcctngTransmitTrafficDescriptorParam5_Object=MibScalar
atmAcctngTransmitTrafficDescriptorParam5=_AtmAcctngTransmitTrafficDescriptorParam5_Object((1,3,6,1,2,1,59,1,1,24),_AtmAcctngTransmitTrafficDescriptorParam5_Type())
atmAcctngTransmitTrafficDescriptorParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngTransmitTrafficDescriptorParam5.setStatus(_A)
_AtmAcctngReceiveTrafficDescriptorType_Type=ObjectIdentifier
_AtmAcctngReceiveTrafficDescriptorType_Object=MibScalar
atmAcctngReceiveTrafficDescriptorType=_AtmAcctngReceiveTrafficDescriptorType_Object((1,3,6,1,2,1,59,1,1,25),_AtmAcctngReceiveTrafficDescriptorType_Type())
atmAcctngReceiveTrafficDescriptorType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceiveTrafficDescriptorType.setStatus(_A)
class _AtmAcctngReceiveTrafficDescriptorParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngReceiveTrafficDescriptorParam1_Type.__name__=_C
_AtmAcctngReceiveTrafficDescriptorParam1_Object=MibScalar
atmAcctngReceiveTrafficDescriptorParam1=_AtmAcctngReceiveTrafficDescriptorParam1_Object((1,3,6,1,2,1,59,1,1,26),_AtmAcctngReceiveTrafficDescriptorParam1_Type())
atmAcctngReceiveTrafficDescriptorParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceiveTrafficDescriptorParam1.setStatus(_A)
class _AtmAcctngReceiveTrafficDescriptorParam2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngReceiveTrafficDescriptorParam2_Type.__name__=_C
_AtmAcctngReceiveTrafficDescriptorParam2_Object=MibScalar
atmAcctngReceiveTrafficDescriptorParam2=_AtmAcctngReceiveTrafficDescriptorParam2_Object((1,3,6,1,2,1,59,1,1,27),_AtmAcctngReceiveTrafficDescriptorParam2_Type())
atmAcctngReceiveTrafficDescriptorParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceiveTrafficDescriptorParam2.setStatus(_A)
class _AtmAcctngReceiveTrafficDescriptorParam3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngReceiveTrafficDescriptorParam3_Type.__name__=_C
_AtmAcctngReceiveTrafficDescriptorParam3_Object=MibScalar
atmAcctngReceiveTrafficDescriptorParam3=_AtmAcctngReceiveTrafficDescriptorParam3_Object((1,3,6,1,2,1,59,1,1,28),_AtmAcctngReceiveTrafficDescriptorParam3_Type())
atmAcctngReceiveTrafficDescriptorParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceiveTrafficDescriptorParam3.setStatus(_A)
class _AtmAcctngReceiveTrafficDescriptorParam4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngReceiveTrafficDescriptorParam4_Type.__name__=_C
_AtmAcctngReceiveTrafficDescriptorParam4_Object=MibScalar
atmAcctngReceiveTrafficDescriptorParam4=_AtmAcctngReceiveTrafficDescriptorParam4_Object((1,3,6,1,2,1,59,1,1,29),_AtmAcctngReceiveTrafficDescriptorParam4_Type())
atmAcctngReceiveTrafficDescriptorParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceiveTrafficDescriptorParam4.setStatus(_A)
class _AtmAcctngReceiveTrafficDescriptorParam5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AtmAcctngReceiveTrafficDescriptorParam5_Type.__name__=_C
_AtmAcctngReceiveTrafficDescriptorParam5_Object=MibScalar
atmAcctngReceiveTrafficDescriptorParam5=_AtmAcctngReceiveTrafficDescriptorParam5_Object((1,3,6,1,2,1,59,1,1,30),_AtmAcctngReceiveTrafficDescriptorParam5_Type())
atmAcctngReceiveTrafficDescriptorParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngReceiveTrafficDescriptorParam5.setStatus(_A)
_AtmAcctngCallingPartySubAddress_Type=AtmAddr
_AtmAcctngCallingPartySubAddress_Object=MibScalar
atmAcctngCallingPartySubAddress=_AtmAcctngCallingPartySubAddress_Object((1,3,6,1,2,1,59,1,1,31),_AtmAcctngCallingPartySubAddress_Type())
atmAcctngCallingPartySubAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCallingPartySubAddress.setStatus(_A)
_AtmAcctngCalledPartySubAddress_Type=AtmAddr
_AtmAcctngCalledPartySubAddress_Object=MibScalar
atmAcctngCalledPartySubAddress=_AtmAcctngCalledPartySubAddress_Object((1,3,6,1,2,1,59,1,1,32),_AtmAcctngCalledPartySubAddress_Type())
atmAcctngCalledPartySubAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngCalledPartySubAddress.setStatus(_A)
class _AtmAcctngRecordCrc16_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AtmAcctngRecordCrc16_Type.__name__=_D
_AtmAcctngRecordCrc16_Object=MibScalar
atmAcctngRecordCrc16=_AtmAcctngRecordCrc16_Object((1,3,6,1,2,1,59,1,1,33),_AtmAcctngRecordCrc16_Type())
atmAcctngRecordCrc16.setMaxAccess(_B)
if mibBuilder.loadTexts:atmAcctngRecordCrc16.setStatus(_A)
mibBuilder.exportSymbols('ATM-ACCOUNTING-INFORMATION-MIB',**{'atmAccountingInformationMIB':atmAccountingInformationMIB,'atmAcctngMIBObjects':atmAcctngMIBObjects,'atmAcctngDataObjects':atmAcctngDataObjects,'atmAcctngConnectionType':atmAcctngConnectionType,'atmAcctngCastType':atmAcctngCastType,'atmAcctngIfName':atmAcctngIfName,'atmAcctngIfAlias':atmAcctngIfAlias,'atmAcctngVpi':atmAcctngVpi,'atmAcctngVci':atmAcctngVci,'atmAcctngCallingParty':atmAcctngCallingParty,'atmAcctngCalledParty':atmAcctngCalledParty,'atmAcctngCallReference':atmAcctngCallReference,'atmAcctngStartTime':atmAcctngStartTime,'atmAcctngCollectionTime':atmAcctngCollectionTime,'atmAcctngCollectMode':atmAcctngCollectMode,'atmAcctngReleaseCause':atmAcctngReleaseCause,'atmAcctngServiceCategory':atmAcctngServiceCategory,'atmAcctngTransmittedCells':atmAcctngTransmittedCells,'atmAcctngTransmittedClp0Cells':atmAcctngTransmittedClp0Cells,'atmAcctngReceivedCells':atmAcctngReceivedCells,'atmAcctngReceivedClp0Cells':atmAcctngReceivedClp0Cells,'atmAcctngTransmitTrafficDescriptorType':atmAcctngTransmitTrafficDescriptorType,'atmAcctngTransmitTrafficDescriptorParam1':atmAcctngTransmitTrafficDescriptorParam1,'atmAcctngTransmitTrafficDescriptorParam2':atmAcctngTransmitTrafficDescriptorParam2,'atmAcctngTransmitTrafficDescriptorParam3':atmAcctngTransmitTrafficDescriptorParam3,'atmAcctngTransmitTrafficDescriptorParam4':atmAcctngTransmitTrafficDescriptorParam4,'atmAcctngTransmitTrafficDescriptorParam5':atmAcctngTransmitTrafficDescriptorParam5,'atmAcctngReceiveTrafficDescriptorType':atmAcctngReceiveTrafficDescriptorType,'atmAcctngReceiveTrafficDescriptorParam1':atmAcctngReceiveTrafficDescriptorParam1,'atmAcctngReceiveTrafficDescriptorParam2':atmAcctngReceiveTrafficDescriptorParam2,'atmAcctngReceiveTrafficDescriptorParam3':atmAcctngReceiveTrafficDescriptorParam3,'atmAcctngReceiveTrafficDescriptorParam4':atmAcctngReceiveTrafficDescriptorParam4,'atmAcctngReceiveTrafficDescriptorParam5':atmAcctngReceiveTrafficDescriptorParam5,'atmAcctngCallingPartySubAddress':atmAcctngCallingPartySubAddress,'atmAcctngCalledPartySubAddress':atmAcctngCalledPartySubAddress,'atmAcctngRecordCrc16':atmAcctngRecordCrc16})