_D='fsPoePdMacAddress'
_C='SUPERMICRO-POE-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fspoe=ModuleIdentity((1,3,6,1,4,1,10876,101,1,103))
if mibBuilder.loadTexts:fspoe.setRevisions(('2012-09-05 00:00',))
_FsPoeSystem_ObjectIdentity=ObjectIdentity
fsPoeSystem=_FsPoeSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,1,103,1))
class _FsPoeGlobalAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsPoeGlobalAdminStatus_Type.__name__=_B
_FsPoeGlobalAdminStatus_Object=MibScalar
fsPoeGlobalAdminStatus=_FsPoeGlobalAdminStatus_Object((1,3,6,1,4,1,10876,101,1,103,1,1),_FsPoeGlobalAdminStatus_Type())
fsPoeGlobalAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsPoeGlobalAdminStatus.setStatus(_A)
_FsPoeMacTable_Object=MibTable
fsPoeMacTable=_FsPoeMacTable_Object((1,3,6,1,4,1,10876,101,1,103,1,2))
if mibBuilder.loadTexts:fsPoeMacTable.setStatus(_A)
_FsPoeMacEntry_Object=MibTableRow
fsPoeMacEntry=_FsPoeMacEntry_Object((1,3,6,1,4,1,10876,101,1,103,1,2,1))
fsPoeMacEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fsPoeMacEntry.setStatus(_A)
_FsPoePdMacAddress_Type=MacAddress
_FsPoePdMacAddress_Object=MibTableColumn
fsPoePdMacAddress=_FsPoePdMacAddress_Object((1,3,6,1,4,1,10876,101,1,103,1,2,1,1),_FsPoePdMacAddress_Type())
fsPoePdMacAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsPoePdMacAddress.setStatus(_A)
_FsPoePdMacPort_Type=InterfaceIndex
_FsPoePdMacPort_Object=MibTableColumn
fsPoePdMacPort=_FsPoePdMacPort_Object((1,3,6,1,4,1,10876,101,1,103,1,2,1,2),_FsPoePdMacPort_Type())
fsPoePdMacPort.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsPoePdMacPort.setStatus(_A)
_FsPoePdMacRowStatus_Type=RowStatus
_FsPoePdMacRowStatus_Object=MibTableColumn
fsPoePdMacRowStatus=_FsPoePdMacRowStatus_Object((1,3,6,1,4,1,10876,101,1,103,1,2,1,3),_FsPoePdMacRowStatus_Type())
fsPoePdMacRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsPoePdMacRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fspoe':fspoe,'fsPoeSystem':fsPoeSystem,'fsPoeGlobalAdminStatus':fsPoeGlobalAdminStatus,'fsPoeMacTable':fsPoeMacTable,'fsPoeMacEntry':fsPoeMacEntry,_D:fsPoePdMacAddress,'fsPoePdMacPort':fsPoePdMacPort,'fsPoePdMacRowStatus':fsPoePdMacRowStatus})