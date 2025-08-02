_G='pppoeAcServiceEthIfIndex'
_F='delete'
_E='pppoeAcEthIfIndex'
_D='BIANCA-BRICK-PPPOEAC-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Pppoe_ObjectIdentity=ObjectIdentity
pppoe=_Pppoe_ObjectIdentity((1,3,6,1,4,1,272,4,24))
_PppoeAcTable_Object=MibTable
pppoeAcTable=_PppoeAcTable_Object((1,3,6,1,4,1,272,4,24,3))
if mibBuilder.loadTexts:pppoeAcTable.setStatus(_A)
_PppoeAcEntry_Object=MibTableRow
pppoeAcEntry=_PppoeAcEntry_Object((1,3,6,1,4,1,272,4,24,3,1))
pppoeAcEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pppoeAcEntry.setStatus(_A)
_PppoeAcEthIfIndex_Type=Integer32
_PppoeAcEthIfIndex_Object=MibTableColumn
pppoeAcEthIfIndex=_PppoeAcEthIfIndex_Object((1,3,6,1,4,1,272,4,24,3,1,1),_PppoeAcEthIfIndex_Type())
pppoeAcEthIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeAcEthIfIndex.setStatus(_A)
class _PppoeAcChkService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('accept-all',1),('accept-from-list',2),(_F,4)))
_PppoeAcChkService_Type.__name__=_C
_PppoeAcChkService_Object=MibTableColumn
pppoeAcChkService=_PppoeAcChkService_Object((1,3,6,1,4,1,272,4,24,3,1,2),_PppoeAcChkService_Type())
pppoeAcChkService.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeAcChkService.setStatus(_A)
_PppoeAcName_Type=DisplayString
_PppoeAcName_Object=MibTableColumn
pppoeAcName=_PppoeAcName_Object((1,3,6,1,4,1,272,4,24,3,1,3),_PppoeAcName_Type())
pppoeAcName.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeAcName.setStatus(_A)
_PppoeAcServiceTable_Object=MibTable
pppoeAcServiceTable=_PppoeAcServiceTable_Object((1,3,6,1,4,1,272,4,24,4))
if mibBuilder.loadTexts:pppoeAcServiceTable.setStatus(_A)
_PppoeAcServiceEntry_Object=MibTableRow
pppoeAcServiceEntry=_PppoeAcServiceEntry_Object((1,3,6,1,4,1,272,4,24,4,1))
pppoeAcServiceEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:pppoeAcServiceEntry.setStatus(_A)
_PppoeAcServiceEthIfIndex_Type=Integer32
_PppoeAcServiceEthIfIndex_Object=MibTableColumn
pppoeAcServiceEthIfIndex=_PppoeAcServiceEthIfIndex_Object((1,3,6,1,4,1,272,4,24,4,1,1),_PppoeAcServiceEthIfIndex_Type())
pppoeAcServiceEthIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeAcServiceEthIfIndex.setStatus(_A)
_PppoeAcServiceName_Type=DisplayString
_PppoeAcServiceName_Object=MibTableColumn
pppoeAcServiceName=_PppoeAcServiceName_Object((1,3,6,1,4,1,272,4,24,4,1,2),_PppoeAcServiceName_Type())
pppoeAcServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeAcServiceName.setStatus(_A)
class _PppoeAcServiceStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),(_F,3)))
_PppoeAcServiceStatus_Type.__name__=_C
_PppoeAcServiceStatus_Object=MibTableColumn
pppoeAcServiceStatus=_PppoeAcServiceStatus_Object((1,3,6,1,4,1,272,4,24,4,1,3),_PppoeAcServiceStatus_Type())
pppoeAcServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pppoeAcServiceStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bintec':bintec,'bibo':bibo,'pppoe':pppoe,'pppoeAcTable':pppoeAcTable,'pppoeAcEntry':pppoeAcEntry,_E:pppoeAcEthIfIndex,'pppoeAcChkService':pppoeAcChkService,'pppoeAcName':pppoeAcName,'pppoeAcServiceTable':pppoeAcServiceTable,'pppoeAcServiceEntry':pppoeAcServiceEntry,_G:pppoeAcServiceEthIfIndex,'pppoeAcServiceName':pppoeAcServiceName,'pppoeAcServiceStatus':pppoeAcServiceStatus})