_F='read-only'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortInfoIndex,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortInfoIndex')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adGenTa5kOam,adGenTa5kOamID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kOam','adGenTa5kOamID')
atmVclVci,atmVclVpi=mibBuilder.importSymbols('ATM-MIB','atmVclVci','atmVclVpi')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
adTa5kOamModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,20,1))
if mibBuilder.loadTexts:adTa5kOamModuleIdentity.setRevisions(('2014-05-05 00:00',))
_AdGenTa5kOamTable_Object=MibTable
adGenTa5kOamTable=_AdGenTa5kOamTable_Object((1,3,6,1,4,1,664,5,67,1,20,1))
if mibBuilder.loadTexts:adGenTa5kOamTable.setStatus(_A)
_AdGenTa5kOamEntry_Object=MibTableRow
adGenTa5kOamEntry=_AdGenTa5kOamEntry_Object((1,3,6,1,4,1,664,5,67,1,20,1,1))
adGenTa5kOamEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenTa5kOamEntry.setStatus(_A)
_AdGenTa5kOamLBIfId_Type=InterfaceIndex
_AdGenTa5kOamLBIfId_Object=MibTableColumn
adGenTa5kOamLBIfId=_AdGenTa5kOamLBIfId_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,1),_AdGenTa5kOamLBIfId_Type())
adGenTa5kOamLBIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBIfId.setStatus(_A)
class _AdGenTa5kOamLBVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AdGenTa5kOamLBVpi_Type.__name__=_C
_AdGenTa5kOamLBVpi_Object=MibTableColumn
adGenTa5kOamLBVpi=_AdGenTa5kOamLBVpi_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,2),_AdGenTa5kOamLBVpi_Type())
adGenTa5kOamLBVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBVpi.setStatus(_A)
class _AdGenTa5kOamLBVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AdGenTa5kOamLBVci_Type.__name__=_C
_AdGenTa5kOamLBVci_Object=MibTableColumn
adGenTa5kOamLBVci=_AdGenTa5kOamLBVci_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,3),_AdGenTa5kOamLBVci_Type())
adGenTa5kOamLBVci.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBVci.setStatus(_A)
class _AdGenTa5kOamLBType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('segment',1),('end-to-end',2)))
_AdGenTa5kOamLBType_Type.__name__=_C
_AdGenTa5kOamLBType_Object=MibTableColumn
adGenTa5kOamLBType=_AdGenTa5kOamLBType_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,4),_AdGenTa5kOamLBType_Type())
adGenTa5kOamLBType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBType.setStatus(_A)
_AdGenTa5kOamLBDestLlid_Type=OctetString
_AdGenTa5kOamLBDestLlid_Object=MibTableColumn
adGenTa5kOamLBDestLlid=_AdGenTa5kOamLBDestLlid_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,5),_AdGenTa5kOamLBDestLlid_Type())
adGenTa5kOamLBDestLlid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBDestLlid.setStatus(_A)
_AdGenTa5kOamLBSend_Type=Integer32
_AdGenTa5kOamLBSend_Object=MibTableColumn
adGenTa5kOamLBSend=_AdGenTa5kOamLBSend_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,6),_AdGenTa5kOamLBSend_Type())
adGenTa5kOamLBSend.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBSend.setStatus(_A)
_AdGenTa5kOamLBResetCounts_Type=Integer32
_AdGenTa5kOamLBResetCounts_Object=MibTableColumn
adGenTa5kOamLBResetCounts=_AdGenTa5kOamLBResetCounts_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,7),_AdGenTa5kOamLBResetCounts_Type())
adGenTa5kOamLBResetCounts.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBResetCounts.setStatus(_A)
_AdGenTa5kOamLocalLlid_Type=OctetString
_AdGenTa5kOamLocalLlid_Object=MibTableColumn
adGenTa5kOamLocalLlid=_AdGenTa5kOamLocalLlid_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,8),_AdGenTa5kOamLocalLlid_Type())
adGenTa5kOamLocalLlid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLocalLlid.setStatus(_A)
_AdGenTa5kOamLBTxRequests_Type=Integer32
_AdGenTa5kOamLBTxRequests_Object=MibTableColumn
adGenTa5kOamLBTxRequests=_AdGenTa5kOamLBTxRequests_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,9),_AdGenTa5kOamLBTxRequests_Type())
adGenTa5kOamLBTxRequests.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenTa5kOamLBTxRequests.setStatus(_A)
_AdGenTa5kOamLBRxResponses_Type=Integer32
_AdGenTa5kOamLBRxResponses_Object=MibTableColumn
adGenTa5kOamLBRxResponses=_AdGenTa5kOamLBRxResponses_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,10),_AdGenTa5kOamLBRxResponses_Type())
adGenTa5kOamLBRxResponses.setMaxAccess(_F)
if mibBuilder.loadTexts:adGenTa5kOamLBRxResponses.setStatus(_A)
class _AdGenTa5kOamLBSendSpecifiedNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_AdGenTa5kOamLBSendSpecifiedNumber_Type.__name__=_C
_AdGenTa5kOamLBSendSpecifiedNumber_Object=MibTableColumn
adGenTa5kOamLBSendSpecifiedNumber=_AdGenTa5kOamLBSendSpecifiedNumber_Object((1,3,6,1,4,1,664,5,67,1,20,1,1,11),_AdGenTa5kOamLBSendSpecifiedNumber_Type())
adGenTa5kOamLBSendSpecifiedNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenTa5kOamLBSendSpecifiedNumber.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-OAM-MIB',**{'adGenTa5kOamTable':adGenTa5kOamTable,'adGenTa5kOamEntry':adGenTa5kOamEntry,'adGenTa5kOamLBIfId':adGenTa5kOamLBIfId,'adGenTa5kOamLBVpi':adGenTa5kOamLBVpi,'adGenTa5kOamLBVci':adGenTa5kOamLBVci,'adGenTa5kOamLBType':adGenTa5kOamLBType,'adGenTa5kOamLBDestLlid':adGenTa5kOamLBDestLlid,'adGenTa5kOamLBSend':adGenTa5kOamLBSend,'adGenTa5kOamLBResetCounts':adGenTa5kOamLBResetCounts,'adGenTa5kOamLocalLlid':adGenTa5kOamLocalLlid,'adGenTa5kOamLBTxRequests':adGenTa5kOamLBTxRequests,'adGenTa5kOamLBRxResponses':adGenTa5kOamLBRxResponses,'adGenTa5kOamLBSendSpecifiedNumber':adGenTa5kOamLBSendSpecifiedNumber,'adTa5kOamModuleIdentity':adTa5kOamModuleIdentity})