_H='fdryTacacsServerIndex'
_G='FDRY-TACACS-MIB'
_F='DisplayString'
_E='Unsigned32'
_D='InetAddressType'
_C='ServerUsage'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ServerUsage,=mibBuilder.importSymbols('FDRY-RADIUS-MIB',_C)
fdryTacacs,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','fdryTacacs')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
fdryTacacsMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,9,1))
if mibBuilder.loadTexts:fdryTacacsMIB.setRevisions(('2008-02-25 00:00','2017-08-07 00:00'))
class InetAddress(TextualConvention,OctetString):status=_A;displayHint='1x ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FdryTacacsServer_ObjectIdentity=ObjectIdentity
fdryTacacsServer=_FdryTacacsServer_ObjectIdentity((1,3,6,1,4,1,1991,1,1,9,1,1))
_FdryTacacsServerTable_Object=MibTable
fdryTacacsServerTable=_FdryTacacsServerTable_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1))
if mibBuilder.loadTexts:fdryTacacsServerTable.setStatus(_A)
_FdryTacacsServerEntry_Object=MibTableRow
fdryTacacsServerEntry=_FdryTacacsServerEntry_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1))
fdryTacacsServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fdryTacacsServerEntry.setStatus(_A)
_FdryTacacsServerIndex_Type=Unsigned32
_FdryTacacsServerIndex_Object=MibTableColumn
fdryTacacsServerIndex=_FdryTacacsServerIndex_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1,1),_FdryTacacsServerIndex_Type())
fdryTacacsServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fdryTacacsServerIndex.setStatus(_A)
class _FdryTacacsServerAddrType_Type(InetAddressType):defaultValue=1
_FdryTacacsServerAddrType_Type.__name__=_D
_FdryTacacsServerAddrType_Object=MibTableColumn
fdryTacacsServerAddrType=_FdryTacacsServerAddrType_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1,2),_FdryTacacsServerAddrType_Type())
fdryTacacsServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTacacsServerAddrType.setStatus(_A)
_FdryTacacsServerAddr_Type=InetAddress
_FdryTacacsServerAddr_Object=MibTableColumn
fdryTacacsServerAddr=_FdryTacacsServerAddr_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1,3),_FdryTacacsServerAddr_Type())
fdryTacacsServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTacacsServerAddr.setStatus(_A)
class _FdryTacacsServerAuthPort_Type(Unsigned32):defaultValue=49
_FdryTacacsServerAuthPort_Type.__name__=_E
_FdryTacacsServerAuthPort_Object=MibTableColumn
fdryTacacsServerAuthPort=_FdryTacacsServerAuthPort_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1,4),_FdryTacacsServerAuthPort_Type())
fdryTacacsServerAuthPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTacacsServerAuthPort.setStatus(_A)
class _FdryTacacsServerRowKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FdryTacacsServerRowKey_Type.__name__=_F
_FdryTacacsServerRowKey_Object=MibTableColumn
fdryTacacsServerRowKey=_FdryTacacsServerRowKey_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1,5),_FdryTacacsServerRowKey_Type())
fdryTacacsServerRowKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTacacsServerRowKey.setStatus(_A)
class _FdryTacacsServerUsage_Type(ServerUsage):defaultValue=1
_FdryTacacsServerUsage_Type.__name__=_C
_FdryTacacsServerUsage_Object=MibTableColumn
fdryTacacsServerUsage=_FdryTacacsServerUsage_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1,6),_FdryTacacsServerUsage_Type())
fdryTacacsServerUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTacacsServerUsage.setStatus(_A)
_FdryTacacsServerRowStatus_Type=RowStatus
_FdryTacacsServerRowStatus_Object=MibTableColumn
fdryTacacsServerRowStatus=_FdryTacacsServerRowStatus_Object((1,3,6,1,4,1,1991,1,1,9,1,1,1,1,7),_FdryTacacsServerRowStatus_Type())
fdryTacacsServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTacacsServerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'InetAddress':InetAddress,'fdryTacacsMIB':fdryTacacsMIB,'fdryTacacsServer':fdryTacacsServer,'fdryTacacsServerTable':fdryTacacsServerTable,'fdryTacacsServerEntry':fdryTacacsServerEntry,_H:fdryTacacsServerIndex,'fdryTacacsServerAddrType':fdryTacacsServerAddrType,'fdryTacacsServerAddr':fdryTacacsServerAddr,'fdryTacacsServerAuthPort':fdryTacacsServerAuthPort,'fdryTacacsServerRowKey':fdryTacacsServerRowKey,'fdryTacacsServerUsage':fdryTacacsServerUsage,'fdryTacacsServerRowStatus':fdryTacacsServerRowStatus})