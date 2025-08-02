_H='slSecuEncryptionIfIndex'
_G='slSecuWlIp'
_F='slSecuSelectType'
_E='Integer32'
_D='SL-SECU-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
slSecuMib=ModuleIdentity((1,3,6,1,4,1,4515,1,3,24))
class SlSecuType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('telnet',1),('ssh',2),('http',3),('https',4),('icmp',5),('snmp',6),('ftp',7),('tftp',8),('tl1',9),('tl1ssh',10),('wl',11)))
_SlSecuGen_ObjectIdentity=ObjectIdentity
slSecuGen=_SlSecuGen_ObjectIdentity((1,3,6,1,4,1,4515,1,3,24,1))
_SlSecuFirewallEnable_Type=TruthValue
_SlSecuFirewallEnable_Object=MibScalar
slSecuFirewallEnable=_SlSecuFirewallEnable_Object((1,3,6,1,4,1,4515,1,3,24,1,1),_SlSecuFirewallEnable_Type())
slSecuFirewallEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:slSecuFirewallEnable.setStatus(_A)
_SlSecuSelect_ObjectIdentity=ObjectIdentity
slSecuSelect=_SlSecuSelect_ObjectIdentity((1,3,6,1,4,1,4515,1,3,24,2))
_SlSecuSelectTable_Object=MibTable
slSecuSelectTable=_SlSecuSelectTable_Object((1,3,6,1,4,1,4515,1,3,24,2,1))
if mibBuilder.loadTexts:slSecuSelectTable.setStatus(_A)
_SlSecuSelectEntry_Object=MibTableRow
slSecuSelectEntry=_SlSecuSelectEntry_Object((1,3,6,1,4,1,4515,1,3,24,2,1,1))
slSecuSelectEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:slSecuSelectEntry.setStatus(_A)
_SlSecuSelectType_Type=SlSecuType
_SlSecuSelectType_Object=MibTableColumn
slSecuSelectType=_SlSecuSelectType_Object((1,3,6,1,4,1,4515,1,3,24,2,1,1,1),_SlSecuSelectType_Type())
slSecuSelectType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:slSecuSelectType.setStatus(_A)
_SlSecuSelectPort_Type=Integer32
_SlSecuSelectPort_Object=MibTableColumn
slSecuSelectPort=_SlSecuSelectPort_Object((1,3,6,1,4,1,4515,1,3,24,2,1,1,2),_SlSecuSelectPort_Type())
slSecuSelectPort.setMaxAccess(_C)
if mibBuilder.loadTexts:slSecuSelectPort.setStatus(_A)
_SlSecuSelectEnable_Type=TruthValue
_SlSecuSelectEnable_Object=MibTableColumn
slSecuSelectEnable=_SlSecuSelectEnable_Object((1,3,6,1,4,1,4515,1,3,24,2,1,1,3),_SlSecuSelectEnable_Type())
slSecuSelectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:slSecuSelectEnable.setStatus(_A)
_SlSecuWl_ObjectIdentity=ObjectIdentity
slSecuWl=_SlSecuWl_ObjectIdentity((1,3,6,1,4,1,4515,1,3,24,3))
_SlSecuWlTable_Object=MibTable
slSecuWlTable=_SlSecuWlTable_Object((1,3,6,1,4,1,4515,1,3,24,3,1))
if mibBuilder.loadTexts:slSecuWlTable.setStatus(_A)
_SlSecuWlEntry_Object=MibTableRow
slSecuWlEntry=_SlSecuWlEntry_Object((1,3,6,1,4,1,4515,1,3,24,3,1,1))
slSecuWlEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:slSecuWlEntry.setStatus(_A)
_SlSecuWlIp_Type=IpAddress
_SlSecuWlIp_Object=MibTableColumn
slSecuWlIp=_SlSecuWlIp_Object((1,3,6,1,4,1,4515,1,3,24,3,1,1,1),_SlSecuWlIp_Type())
slSecuWlIp.setMaxAccess(_C)
if mibBuilder.loadTexts:slSecuWlIp.setStatus(_A)
_SlSecuWlMask_Type=IpAddress
_SlSecuWlMask_Object=MibTableColumn
slSecuWlMask=_SlSecuWlMask_Object((1,3,6,1,4,1,4515,1,3,24,3,1,1,2),_SlSecuWlMask_Type())
slSecuWlMask.setMaxAccess(_C)
if mibBuilder.loadTexts:slSecuWlMask.setStatus(_A)
_SlSecuWlStatus_Type=RowStatus
_SlSecuWlStatus_Object=MibTableColumn
slSecuWlStatus=_SlSecuWlStatus_Object((1,3,6,1,4,1,4515,1,3,24,3,1,1,3),_SlSecuWlStatus_Type())
slSecuWlStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:slSecuWlStatus.setStatus(_A)
_SlSecuEncryption_ObjectIdentity=ObjectIdentity
slSecuEncryption=_SlSecuEncryption_ObjectIdentity((1,3,6,1,4,1,4515,1,3,24,4))
_SlSecuEncryptionTable_Object=MibTable
slSecuEncryptionTable=_SlSecuEncryptionTable_Object((1,3,6,1,4,1,4515,1,3,24,4,1))
if mibBuilder.loadTexts:slSecuEncryptionTable.setStatus(_A)
_SlSecuEncryptionEntry_Object=MibTableRow
slSecuEncryptionEntry=_SlSecuEncryptionEntry_Object((1,3,6,1,4,1,4515,1,3,24,4,1,1))
slSecuEncryptionEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:slSecuEncryptionEntry.setStatus(_A)
_SlSecuEncryptionIfIndex_Type=InterfaceIndex
_SlSecuEncryptionIfIndex_Object=MibTableColumn
slSecuEncryptionIfIndex=_SlSecuEncryptionIfIndex_Object((1,3,6,1,4,1,4515,1,3,24,4,1,1,1),_SlSecuEncryptionIfIndex_Type())
slSecuEncryptionIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slSecuEncryptionIfIndex.setStatus(_A)
_SlSecuEncryptionEnable_Type=TruthValue
_SlSecuEncryptionEnable_Object=MibTableColumn
slSecuEncryptionEnable=_SlSecuEncryptionEnable_Object((1,3,6,1,4,1,4515,1,3,24,4,1,1,2),_SlSecuEncryptionEnable_Type())
slSecuEncryptionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:slSecuEncryptionEnable.setStatus(_A)
class _SlSecuEncryptionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('exchange',2),('kdf',3),('active',4)))
_SlSecuEncryptionStatus_Type.__name__=_E
_SlSecuEncryptionStatus_Object=MibTableColumn
slSecuEncryptionStatus=_SlSecuEncryptionStatus_Object((1,3,6,1,4,1,4515,1,3,24,4,1,1,3),_SlSecuEncryptionStatus_Type())
slSecuEncryptionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slSecuEncryptionStatus.setStatus(_A)
_SlSecuEncryptionForceInit_Type=Integer32
_SlSecuEncryptionForceInit_Object=MibTableColumn
slSecuEncryptionForceInit=_SlSecuEncryptionForceInit_Object((1,3,6,1,4,1,4515,1,3,24,4,1,1,4),_SlSecuEncryptionForceInit_Type())
slSecuEncryptionForceInit.setMaxAccess(_B)
if mibBuilder.loadTexts:slSecuEncryptionForceInit.setStatus(_A)
_SlSecuEncryptionPreShared_Type=DisplayString
_SlSecuEncryptionPreShared_Object=MibTableColumn
slSecuEncryptionPreShared=_SlSecuEncryptionPreShared_Object((1,3,6,1,4,1,4515,1,3,24,4,1,1,5),_SlSecuEncryptionPreShared_Type())
slSecuEncryptionPreShared.setMaxAccess(_B)
if mibBuilder.loadTexts:slSecuEncryptionPreShared.setStatus(_A)
_SlSecuEncryptionKeyExchangePeriod_Type=Integer32
_SlSecuEncryptionKeyExchangePeriod_Object=MibTableColumn
slSecuEncryptionKeyExchangePeriod=_SlSecuEncryptionKeyExchangePeriod_Object((1,3,6,1,4,1,4515,1,3,24,4,1,1,6),_SlSecuEncryptionKeyExchangePeriod_Type())
slSecuEncryptionKeyExchangePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:slSecuEncryptionKeyExchangePeriod.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'SlSecuType':SlSecuType,'slSecuMib':slSecuMib,'slSecuGen':slSecuGen,'slSecuFirewallEnable':slSecuFirewallEnable,'slSecuSelect':slSecuSelect,'slSecuSelectTable':slSecuSelectTable,'slSecuSelectEntry':slSecuSelectEntry,_F:slSecuSelectType,'slSecuSelectPort':slSecuSelectPort,'slSecuSelectEnable':slSecuSelectEnable,'slSecuWl':slSecuWl,'slSecuWlTable':slSecuWlTable,'slSecuWlEntry':slSecuWlEntry,_G:slSecuWlIp,'slSecuWlMask':slSecuWlMask,'slSecuWlStatus':slSecuWlStatus,'slSecuEncryption':slSecuEncryption,'slSecuEncryptionTable':slSecuEncryptionTable,'slSecuEncryptionEntry':slSecuEncryptionEntry,_H:slSecuEncryptionIfIndex,'slSecuEncryptionEnable':slSecuEncryptionEnable,'slSecuEncryptionStatus':slSecuEncryptionStatus,'slSecuEncryptionForceInit':slSecuEncryptionForceInit,'slSecuEncryptionPreShared':slSecuEncryptionPreShared,'slSecuEncryptionKeyExchangePeriod':slSecuEncryptionKeyExchangePeriod})