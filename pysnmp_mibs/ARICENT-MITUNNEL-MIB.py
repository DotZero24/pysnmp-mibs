_Q='fsMITunlIfConfigID'
_P='fsMITunlIfEncapsMethod'
_O='fsMITunlIfRemoteInetAddress'
_N='fsMITunlIfLocalInetAddress'
_M='fsMITunlIfAddressType'
_L='DisplayString'
_K='Unsigned32'
_J='fsMIStdIpContextId'
_I='ARICENT-MISTD-IPVX-MIB'
_H='read-only'
_G='TruthValue'
_F='InetAddress'
_E='not-accessible'
_D='ARICENT-MITUNNEL-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMIStdIpContextId,=mibBuilder.importSymbols(_I,_J)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention',_G)
fsMITunlMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,39))
if mibBuilder.loadTexts:fsMITunlMIB.setRevisions(('2012-09-05 00:00',))
class FsMITunlType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('other',1),('direct',2),('gre',3),('minimal',4),('l2tp',5),('pptp',6),('l2f',7),('udp',8),('atmp',9),('msdp',10),('sixToFour',11),('sixOverFour',12),('isatap',13),('teredo',14),('compat',15),('ipv6ip',16)))
class FsIPv6FlowLabelOrAny(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1048575))
_FsMITunlMIBObjects_ObjectIdentity=ObjectIdentity
fsMITunlMIBObjects=_FsMITunlMIBObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,39,1))
_FsMITunl_ObjectIdentity=ObjectIdentity
fsMITunl=_FsMITunl_ObjectIdentity((1,3,6,1,4,1,29601,2,39,1,1))
_FsMITunlIfTable_Object=MibTable
fsMITunlIfTable=_FsMITunlIfTable_Object((1,3,6,1,4,1,29601,2,39,1,1,1))
if mibBuilder.loadTexts:fsMITunlIfTable.setStatus(_A)
_FsMITunlIfEntry_Object=MibTableRow
fsMITunlIfEntry=_FsMITunlIfEntry_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1))
fsMITunlIfEntry.setIndexNames((0,_I,_J),(0,_D,_M),(0,_D,_N),(0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:fsMITunlIfEntry.setStatus(_A)
_FsMITunlIfAddressType_Type=InetAddressType
_FsMITunlIfAddressType_Object=MibTableColumn
fsMITunlIfAddressType=_FsMITunlIfAddressType_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,1),_FsMITunlIfAddressType_Type())
fsMITunlIfAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMITunlIfAddressType.setStatus(_A)
class _FsMITunlIfLocalInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMITunlIfLocalInetAddress_Type.__name__=_F
_FsMITunlIfLocalInetAddress_Object=MibTableColumn
fsMITunlIfLocalInetAddress=_FsMITunlIfLocalInetAddress_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,2),_FsMITunlIfLocalInetAddress_Type())
fsMITunlIfLocalInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMITunlIfLocalInetAddress.setStatus(_A)
class _FsMITunlIfRemoteInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMITunlIfRemoteInetAddress_Type.__name__=_F
_FsMITunlIfRemoteInetAddress_Object=MibTableColumn
fsMITunlIfRemoteInetAddress=_FsMITunlIfRemoteInetAddress_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,3),_FsMITunlIfRemoteInetAddress_Type())
fsMITunlIfRemoteInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMITunlIfRemoteInetAddress.setStatus(_A)
_FsMITunlIfEncapsMethod_Type=FsMITunlType
_FsMITunlIfEncapsMethod_Object=MibTableColumn
fsMITunlIfEncapsMethod=_FsMITunlIfEncapsMethod_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,4),_FsMITunlIfEncapsMethod_Type())
fsMITunlIfEncapsMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMITunlIfEncapsMethod.setStatus(_A)
class _FsMITunlIfConfigID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsMITunlIfConfigID_Type.__name__=_C
_FsMITunlIfConfigID_Object=MibTableColumn
fsMITunlIfConfigID=_FsMITunlIfConfigID_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,5),_FsMITunlIfConfigID_Type())
fsMITunlIfConfigID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMITunlIfConfigID.setStatus(_A)
class _FsMITunlIfHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMITunlIfHopLimit_Type.__name__=_C
_FsMITunlIfHopLimit_Object=MibTableColumn
fsMITunlIfHopLimit=_FsMITunlIfHopLimit_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,6),_FsMITunlIfHopLimit_Type())
fsMITunlIfHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfHopLimit.setStatus(_A)
class _FsMITunlIfSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ipsec',2),('other',3)))
_FsMITunlIfSecurity_Type.__name__=_C
_FsMITunlIfSecurity_Object=MibTableColumn
fsMITunlIfSecurity=_FsMITunlIfSecurity_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,7),_FsMITunlIfSecurity_Type())
fsMITunlIfSecurity.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMITunlIfSecurity.setStatus(_A)
class _FsMITunlIfTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,63))
_FsMITunlIfTOS_Type.__name__=_C
_FsMITunlIfTOS_Object=MibTableColumn
fsMITunlIfTOS=_FsMITunlIfTOS_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,8),_FsMITunlIfTOS_Type())
fsMITunlIfTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfTOS.setStatus(_A)
_FsMITunlIfFlowLabel_Type=FsIPv6FlowLabelOrAny
_FsMITunlIfFlowLabel_Object=MibTableColumn
fsMITunlIfFlowLabel=_FsMITunlIfFlowLabel_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,9),_FsMITunlIfFlowLabel_Type())
fsMITunlIfFlowLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfFlowLabel.setStatus(_A)
class _FsMITunlIfMTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1280,1500))
_FsMITunlIfMTU_Type.__name__=_C
_FsMITunlIfMTU_Object=MibTableColumn
fsMITunlIfMTU=_FsMITunlIfMTU_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,10),_FsMITunlIfMTU_Type())
fsMITunlIfMTU.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMITunlIfMTU.setStatus(_A)
class _FsMITunlIfDirFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_FsMITunlIfDirFlag_Type.__name__=_C
_FsMITunlIfDirFlag_Object=MibTableColumn
fsMITunlIfDirFlag=_FsMITunlIfDirFlag_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,11),_FsMITunlIfDirFlag_Type())
fsMITunlIfDirFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfDirFlag.setStatus(_A)
class _FsMITunlIfDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('incoming',1),('outgoing',2)))
_FsMITunlIfDirection_Type.__name__=_C
_FsMITunlIfDirection_Object=MibTableColumn
fsMITunlIfDirection=_FsMITunlIfDirection_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,12),_FsMITunlIfDirection_Type())
fsMITunlIfDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfDirection.setStatus(_A)
class _FsMITunlIfEncaplmt_Type(Unsigned32):defaultValue=4
_FsMITunlIfEncaplmt_Type.__name__=_K
_FsMITunlIfEncaplmt_Object=MibTableColumn
fsMITunlIfEncaplmt=_FsMITunlIfEncaplmt_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,13),_FsMITunlIfEncaplmt_Type())
fsMITunlIfEncaplmt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfEncaplmt.setStatus(_A)
class _FsMITunlIfEncapOption_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsMITunlIfEncapOption_Type.__name__=_C
_FsMITunlIfEncapOption_Object=MibTableColumn
fsMITunlIfEncapOption=_FsMITunlIfEncapOption_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,14),_FsMITunlIfEncapOption_Type())
fsMITunlIfEncapOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfEncapOption.setStatus(_A)
_FsMITunlIfIndex_Type=InterfaceIndexOrZero
_FsMITunlIfIndex_Object=MibTableColumn
fsMITunlIfIndex=_FsMITunlIfIndex_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,15),_FsMITunlIfIndex_Type())
fsMITunlIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMITunlIfIndex.setStatus(_A)
class _FsMITunlIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsMITunlIfAlias_Type.__name__=_L
_FsMITunlIfAlias_Object=MibTableColumn
fsMITunlIfAlias=_FsMITunlIfAlias_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,16),_FsMITunlIfAlias_Type())
fsMITunlIfAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfAlias.setStatus(_A)
class _FsMITunlIfCksumFlag_Type(TruthValue):defaultValue=2
_FsMITunlIfCksumFlag_Type.__name__=_G
_FsMITunlIfCksumFlag_Object=MibTableColumn
fsMITunlIfCksumFlag=_FsMITunlIfCksumFlag_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,17),_FsMITunlIfCksumFlag_Type())
fsMITunlIfCksumFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfCksumFlag.setStatus(_A)
class _FsMITunlIfPmtuFlag_Type(TruthValue):defaultValue=2
_FsMITunlIfPmtuFlag_Type.__name__=_G
_FsMITunlIfPmtuFlag_Object=MibTableColumn
fsMITunlIfPmtuFlag=_FsMITunlIfPmtuFlag_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,18),_FsMITunlIfPmtuFlag_Type())
fsMITunlIfPmtuFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMITunlIfPmtuFlag.setStatus(_A)
_FsMITunlIfStatus_Type=RowStatus
_FsMITunlIfStatus_Object=MibTableColumn
fsMITunlIfStatus=_FsMITunlIfStatus_Object((1,3,6,1,4,1,29601,2,39,1,1,1,1,19),_FsMITunlIfStatus_Type())
fsMITunlIfStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsMITunlIfStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'FsMITunlType':FsMITunlType,'FsIPv6FlowLabelOrAny':FsIPv6FlowLabelOrAny,'fsMITunlMIB':fsMITunlMIB,'fsMITunlMIBObjects':fsMITunlMIBObjects,'fsMITunl':fsMITunl,'fsMITunlIfTable':fsMITunlIfTable,'fsMITunlIfEntry':fsMITunlIfEntry,_M:fsMITunlIfAddressType,_N:fsMITunlIfLocalInetAddress,_O:fsMITunlIfRemoteInetAddress,_P:fsMITunlIfEncapsMethod,_Q:fsMITunlIfConfigID,'fsMITunlIfHopLimit':fsMITunlIfHopLimit,'fsMITunlIfSecurity':fsMITunlIfSecurity,'fsMITunlIfTOS':fsMITunlIfTOS,'fsMITunlIfFlowLabel':fsMITunlIfFlowLabel,'fsMITunlIfMTU':fsMITunlIfMTU,'fsMITunlIfDirFlag':fsMITunlIfDirFlag,'fsMITunlIfDirection':fsMITunlIfDirection,'fsMITunlIfEncaplmt':fsMITunlIfEncaplmt,'fsMITunlIfEncapOption':fsMITunlIfEncapOption,'fsMITunlIfIndex':fsMITunlIfIndex,'fsMITunlIfAlias':fsMITunlIfAlias,'fsMITunlIfCksumFlag':fsMITunlIfCksumFlag,'fsMITunlIfPmtuFlag':fsMITunlIfPmtuFlag,'fsMITunlIfStatus':fsMITunlIfStatus})