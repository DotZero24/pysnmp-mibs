_I='ServerUsage'
_H='fdryRadiusServerIndex'
_G='FDRY-RADIUS-MIB'
_F='DisplayString'
_E='InetAddressType'
_D='OctetString'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fdryRadius,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','fdryRadius')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
fdryRadiusMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,8,1))
if mibBuilder.loadTexts:fdryRadiusMIB.setRevisions(('2008-02-25 00:00','2017-08-07 00:00'))
class ServerUsage(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('default',1),('authenticationOnly',2),('authorizationOnly',3),('accountingOnly',4)))
class InetAddress(TextualConvention,OctetString):status=_A;displayHint='1x ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FdryRadiusServer_ObjectIdentity=ObjectIdentity
fdryRadiusServer=_FdryRadiusServer_ObjectIdentity((1,3,6,1,4,1,1991,1,1,8,1,1))
_FdryRadiusServerTable_Object=MibTable
fdryRadiusServerTable=_FdryRadiusServerTable_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1))
if mibBuilder.loadTexts:fdryRadiusServerTable.setStatus(_A)
_FdryRadiusServerEntry_Object=MibTableRow
fdryRadiusServerEntry=_FdryRadiusServerEntry_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1))
fdryRadiusServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fdryRadiusServerEntry.setStatus(_A)
_FdryRadiusServerIndex_Type=Unsigned32
_FdryRadiusServerIndex_Object=MibTableColumn
fdryRadiusServerIndex=_FdryRadiusServerIndex_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,1),_FdryRadiusServerIndex_Type())
fdryRadiusServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fdryRadiusServerIndex.setStatus(_A)
class _FdryRadiusServerAddrType_Type(InetAddressType):defaultValue=1
_FdryRadiusServerAddrType_Type.__name__=_E
_FdryRadiusServerAddrType_Object=MibTableColumn
fdryRadiusServerAddrType=_FdryRadiusServerAddrType_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,2),_FdryRadiusServerAddrType_Type())
fdryRadiusServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerAddrType.setStatus(_A)
_FdryRadiusServerAddr_Type=InetAddress
_FdryRadiusServerAddr_Object=MibTableColumn
fdryRadiusServerAddr=_FdryRadiusServerAddr_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,3),_FdryRadiusServerAddr_Type())
fdryRadiusServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerAddr.setStatus(_A)
class _FdryRadiusServerAuthPort_Type(Unsigned32):defaultValue=1645
_FdryRadiusServerAuthPort_Type.__name__=_C
_FdryRadiusServerAuthPort_Object=MibTableColumn
fdryRadiusServerAuthPort=_FdryRadiusServerAuthPort_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,4),_FdryRadiusServerAuthPort_Type())
fdryRadiusServerAuthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerAuthPort.setStatus(_A)
class _FdryRadiusServerAcctPort_Type(Unsigned32):defaultValue=1646
_FdryRadiusServerAcctPort_Type.__name__=_C
_FdryRadiusServerAcctPort_Object=MibTableColumn
fdryRadiusServerAcctPort=_FdryRadiusServerAcctPort_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,5),_FdryRadiusServerAcctPort_Type())
fdryRadiusServerAcctPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerAcctPort.setStatus(_A)
class _FdryRadiusServerRowKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FdryRadiusServerRowKey_Type.__name__=_F
_FdryRadiusServerRowKey_Object=MibTableColumn
fdryRadiusServerRowKey=_FdryRadiusServerRowKey_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,6),_FdryRadiusServerRowKey_Type())
fdryRadiusServerRowKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerRowKey.setStatus(_A)
class _FdryRadiusServerUsage_Type(ServerUsage):defaultValue=1
_FdryRadiusServerUsage_Type.__name__=_I
_FdryRadiusServerUsage_Object=MibTableColumn
fdryRadiusServerUsage=_FdryRadiusServerUsage_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,7),_FdryRadiusServerUsage_Type())
fdryRadiusServerUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerUsage.setStatus(_A)
_FdryRadiusServerRowStatus_Type=RowStatus
_FdryRadiusServerRowStatus_Object=MibTableColumn
fdryRadiusServerRowStatus=_FdryRadiusServerRowStatus_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,8),_FdryRadiusServerRowStatus_Type())
fdryRadiusServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerRowStatus.setStatus(_A)
class _FdryRadiusServerAuthType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_FdryRadiusServerAuthType_Type.__name__=_D
_FdryRadiusServerAuthType_Object=MibTableColumn
fdryRadiusServerAuthType=_FdryRadiusServerAuthType_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,9),_FdryRadiusServerAuthType_Type())
fdryRadiusServerAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerAuthType.setStatus(_A)
class _FdryRadiusServerPriority_Type(Unsigned32):defaultValue=0
_FdryRadiusServerPriority_Type.__name__=_C
_FdryRadiusServerPriority_Object=MibTableColumn
fdryRadiusServerPriority=_FdryRadiusServerPriority_Object((1,3,6,1,4,1,1991,1,1,8,1,1,1,1,10),_FdryRadiusServerPriority_Type())
fdryRadiusServerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryRadiusServerPriority.setStatus(_A)
mibBuilder.exportSymbols(_G,**{_I:ServerUsage,'InetAddress':InetAddress,'fdryRadiusMIB':fdryRadiusMIB,'fdryRadiusServer':fdryRadiusServer,'fdryRadiusServerTable':fdryRadiusServerTable,'fdryRadiusServerEntry':fdryRadiusServerEntry,_H:fdryRadiusServerIndex,'fdryRadiusServerAddrType':fdryRadiusServerAddrType,'fdryRadiusServerAddr':fdryRadiusServerAddr,'fdryRadiusServerAuthPort':fdryRadiusServerAuthPort,'fdryRadiusServerAcctPort':fdryRadiusServerAcctPort,'fdryRadiusServerRowKey':fdryRadiusServerRowKey,'fdryRadiusServerUsage':fdryRadiusServerUsage,'fdryRadiusServerRowStatus':fdryRadiusServerRowStatus,'fdryRadiusServerAuthType':fdryRadiusServerAuthType,'fdryRadiusServerPriority':fdryRadiusServerPriority})