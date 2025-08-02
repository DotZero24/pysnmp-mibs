_F='fdrySntpServerIndex'
_E='FDRY-SNTP-MIB'
_D='Integer32'
_C='InetAddressType'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fdrySntp,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','fdrySntp')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fdrySntpMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,7,1))
if mibBuilder.loadTexts:fdrySntpMIB.setRevisions(('2017-08-07 00:00',))
_FdrySntpServer_ObjectIdentity=ObjectIdentity
fdrySntpServer=_FdrySntpServer_ObjectIdentity((1,3,6,1,4,1,1991,1,1,7,1,1))
_FdrySntpServerTable_Object=MibTable
fdrySntpServerTable=_FdrySntpServerTable_Object((1,3,6,1,4,1,1991,1,1,7,1,1,1))
if mibBuilder.loadTexts:fdrySntpServerTable.setStatus(_A)
_FdrySntpServerEntry_Object=MibTableRow
fdrySntpServerEntry=_FdrySntpServerEntry_Object((1,3,6,1,4,1,1991,1,1,7,1,1,1,1))
fdrySntpServerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fdrySntpServerEntry.setStatus(_A)
_FdrySntpServerIndex_Type=Unsigned32
_FdrySntpServerIndex_Object=MibTableColumn
fdrySntpServerIndex=_FdrySntpServerIndex_Object((1,3,6,1,4,1,1991,1,1,7,1,1,1,1,1),_FdrySntpServerIndex_Type())
fdrySntpServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fdrySntpServerIndex.setStatus(_A)
class _FdrySntpServerAddrType_Type(InetAddressType):defaultValue=1
_FdrySntpServerAddrType_Type.__name__=_C
_FdrySntpServerAddrType_Object=MibTableColumn
fdrySntpServerAddrType=_FdrySntpServerAddrType_Object((1,3,6,1,4,1,1991,1,1,7,1,1,1,1,2),_FdrySntpServerAddrType_Type())
fdrySntpServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fdrySntpServerAddrType.setStatus(_A)
_FdrySntpServerAddr_Type=InetAddress
_FdrySntpServerAddr_Object=MibTableColumn
fdrySntpServerAddr=_FdrySntpServerAddr_Object((1,3,6,1,4,1,1991,1,1,7,1,1,1,1,3),_FdrySntpServerAddr_Type())
fdrySntpServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fdrySntpServerAddr.setStatus(_A)
class _FdrySntpServerVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FdrySntpServerVersion_Type.__name__=_D
_FdrySntpServerVersion_Object=MibTableColumn
fdrySntpServerVersion=_FdrySntpServerVersion_Object((1,3,6,1,4,1,1991,1,1,7,1,1,1,1,4),_FdrySntpServerVersion_Type())
fdrySntpServerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fdrySntpServerVersion.setStatus(_A)
_FdrySntpServerRowStatus_Type=RowStatus
_FdrySntpServerRowStatus_Object=MibTableColumn
fdrySntpServerRowStatus=_FdrySntpServerRowStatus_Object((1,3,6,1,4,1,1991,1,1,7,1,1,1,1,5),_FdrySntpServerRowStatus_Type())
fdrySntpServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fdrySntpServerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fdrySntpMIB':fdrySntpMIB,'fdrySntpServer':fdrySntpServer,'fdrySntpServerTable':fdrySntpServerTable,'fdrySntpServerEntry':fdrySntpServerEntry,_F:fdrySntpServerIndex,'fdrySntpServerAddrType':fdrySntpServerAddrType,'fdrySntpServerAddr':fdrySntpServerAddr,'fdrySntpServerVersion':fdrySntpServerVersion,'fdrySntpServerRowStatus':fdrySntpServerRowStatus})