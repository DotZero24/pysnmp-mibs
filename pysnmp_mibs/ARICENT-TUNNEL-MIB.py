_N='fsTunlIfConfigID'
_M='fsTunlIfEncapsMethod'
_L='fsTunlIfRemoteInetAddress'
_K='fsTunlIfLocalInetAddress'
_J='fsTunlIfAddressType'
_I='DisplayString'
_H='Unsigned32'
_G='read-only'
_F='TruthValue'
_E='not-accessible'
_D='ARICENT-TUNNEL-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention',_F)
fsTunlMIB=ModuleIdentity((1,3,6,1,4,1,2076,95))
if mibBuilder.loadTexts:fsTunlMIB.setRevisions(('2012-09-05 00:00',))
class FsTunlType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('other',1),('direct',2),('gre',3),('minimal',4),('l2tp',5),('pptp',6),('l2f',7),('udp',8),('atmp',9),('msdp',10),('sixToFour',11),('sixOverFour',12),('isatap',13),('teredo',14),('compat',15),('ipv6ip',16),('openflow',17)))
class FsIPv6FlowLabelOrAny(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1048575))
_FsTunlMIBObjects_ObjectIdentity=ObjectIdentity
fsTunlMIBObjects=_FsTunlMIBObjects_ObjectIdentity((1,3,6,1,4,1,2076,95,1))
_FsTunl_ObjectIdentity=ObjectIdentity
fsTunl=_FsTunl_ObjectIdentity((1,3,6,1,4,1,2076,95,1,1))
_FsTunlIfTable_Object=MibTable
fsTunlIfTable=_FsTunlIfTable_Object((1,3,6,1,4,1,2076,95,1,1,1))
if mibBuilder.loadTexts:fsTunlIfTable.setStatus(_A)
_FsTunlIfEntry_Object=MibTableRow
fsTunlIfEntry=_FsTunlIfEntry_Object((1,3,6,1,4,1,2076,95,1,1,1,1))
fsTunlIfEntry.setIndexNames((0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:fsTunlIfEntry.setStatus(_A)
_FsTunlIfAddressType_Type=InetAddressType
_FsTunlIfAddressType_Object=MibTableColumn
fsTunlIfAddressType=_FsTunlIfAddressType_Object((1,3,6,1,4,1,2076,95,1,1,1,1,1),_FsTunlIfAddressType_Type())
fsTunlIfAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTunlIfAddressType.setStatus(_A)
_FsTunlIfLocalInetAddress_Type=InetAddress
_FsTunlIfLocalInetAddress_Object=MibTableColumn
fsTunlIfLocalInetAddress=_FsTunlIfLocalInetAddress_Object((1,3,6,1,4,1,2076,95,1,1,1,1,2),_FsTunlIfLocalInetAddress_Type())
fsTunlIfLocalInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTunlIfLocalInetAddress.setStatus(_A)
_FsTunlIfRemoteInetAddress_Type=InetAddress
_FsTunlIfRemoteInetAddress_Object=MibTableColumn
fsTunlIfRemoteInetAddress=_FsTunlIfRemoteInetAddress_Object((1,3,6,1,4,1,2076,95,1,1,1,1,3),_FsTunlIfRemoteInetAddress_Type())
fsTunlIfRemoteInetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTunlIfRemoteInetAddress.setStatus(_A)
_FsTunlIfEncapsMethod_Type=FsTunlType
_FsTunlIfEncapsMethod_Object=MibTableColumn
fsTunlIfEncapsMethod=_FsTunlIfEncapsMethod_Object((1,3,6,1,4,1,2076,95,1,1,1,1,4),_FsTunlIfEncapsMethod_Type())
fsTunlIfEncapsMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTunlIfEncapsMethod.setStatus(_A)
class _FsTunlIfConfigID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsTunlIfConfigID_Type.__name__=_C
_FsTunlIfConfigID_Object=MibTableColumn
fsTunlIfConfigID=_FsTunlIfConfigID_Object((1,3,6,1,4,1,2076,95,1,1,1,1,5),_FsTunlIfConfigID_Type())
fsTunlIfConfigID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsTunlIfConfigID.setStatus(_A)
class _FsTunlIfHopLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsTunlIfHopLimit_Type.__name__=_C
_FsTunlIfHopLimit_Object=MibTableColumn
fsTunlIfHopLimit=_FsTunlIfHopLimit_Object((1,3,6,1,4,1,2076,95,1,1,1,1,6),_FsTunlIfHopLimit_Type())
fsTunlIfHopLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfHopLimit.setStatus(_A)
class _FsTunlIfSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('ipsec',2),('other',3)))
_FsTunlIfSecurity_Type.__name__=_C
_FsTunlIfSecurity_Object=MibTableColumn
fsTunlIfSecurity=_FsTunlIfSecurity_Object((1,3,6,1,4,1,2076,95,1,1,1,1,7),_FsTunlIfSecurity_Type())
fsTunlIfSecurity.setMaxAccess(_G)
if mibBuilder.loadTexts:fsTunlIfSecurity.setStatus(_A)
class _FsTunlIfTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,63))
_FsTunlIfTOS_Type.__name__=_C
_FsTunlIfTOS_Object=MibTableColumn
fsTunlIfTOS=_FsTunlIfTOS_Object((1,3,6,1,4,1,2076,95,1,1,1,1,8),_FsTunlIfTOS_Type())
fsTunlIfTOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfTOS.setStatus(_A)
_FsTunlIfFlowLabel_Type=FsIPv6FlowLabelOrAny
_FsTunlIfFlowLabel_Object=MibTableColumn
fsTunlIfFlowLabel=_FsTunlIfFlowLabel_Object((1,3,6,1,4,1,2076,95,1,1,1,1,9),_FsTunlIfFlowLabel_Type())
fsTunlIfFlowLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfFlowLabel.setStatus(_A)
class _FsTunlIfMTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1280,1500))
_FsTunlIfMTU_Type.__name__=_C
_FsTunlIfMTU_Object=MibTableColumn
fsTunlIfMTU=_FsTunlIfMTU_Object((1,3,6,1,4,1,2076,95,1,1,1,1,10),_FsTunlIfMTU_Type())
fsTunlIfMTU.setMaxAccess(_G)
if mibBuilder.loadTexts:fsTunlIfMTU.setStatus(_A)
class _FsTunlIfDirFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_FsTunlIfDirFlag_Type.__name__=_C
_FsTunlIfDirFlag_Object=MibTableColumn
fsTunlIfDirFlag=_FsTunlIfDirFlag_Object((1,3,6,1,4,1,2076,95,1,1,1,1,11),_FsTunlIfDirFlag_Type())
fsTunlIfDirFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfDirFlag.setStatus(_A)
class _FsTunlIfDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('incoming',1),('outgoing',2)))
_FsTunlIfDirection_Type.__name__=_C
_FsTunlIfDirection_Object=MibTableColumn
fsTunlIfDirection=_FsTunlIfDirection_Object((1,3,6,1,4,1,2076,95,1,1,1,1,12),_FsTunlIfDirection_Type())
fsTunlIfDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfDirection.setStatus(_A)
class _FsTunlIfEncaplmt_Type(Unsigned32):defaultValue=4
_FsTunlIfEncaplmt_Type.__name__=_H
_FsTunlIfEncaplmt_Object=MibTableColumn
fsTunlIfEncaplmt=_FsTunlIfEncaplmt_Object((1,3,6,1,4,1,2076,95,1,1,1,1,13),_FsTunlIfEncaplmt_Type())
fsTunlIfEncaplmt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfEncaplmt.setStatus(_A)
class _FsTunlIfEncapOption_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsTunlIfEncapOption_Type.__name__=_C
_FsTunlIfEncapOption_Object=MibTableColumn
fsTunlIfEncapOption=_FsTunlIfEncapOption_Object((1,3,6,1,4,1,2076,95,1,1,1,1,14),_FsTunlIfEncapOption_Type())
fsTunlIfEncapOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfEncapOption.setStatus(_A)
_FsTunlIfIndex_Type=InterfaceIndexOrZero
_FsTunlIfIndex_Object=MibTableColumn
fsTunlIfIndex=_FsTunlIfIndex_Object((1,3,6,1,4,1,2076,95,1,1,1,1,15),_FsTunlIfIndex_Type())
fsTunlIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsTunlIfIndex.setStatus(_A)
class _FsTunlIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsTunlIfAlias_Type.__name__=_I
_FsTunlIfAlias_Object=MibTableColumn
fsTunlIfAlias=_FsTunlIfAlias_Object((1,3,6,1,4,1,2076,95,1,1,1,1,16),_FsTunlIfAlias_Type())
fsTunlIfAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfAlias.setStatus(_A)
class _FsTunlIfCksumFlag_Type(TruthValue):defaultValue=2
_FsTunlIfCksumFlag_Type.__name__=_F
_FsTunlIfCksumFlag_Object=MibTableColumn
fsTunlIfCksumFlag=_FsTunlIfCksumFlag_Object((1,3,6,1,4,1,2076,95,1,1,1,1,17),_FsTunlIfCksumFlag_Type())
fsTunlIfCksumFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfCksumFlag.setStatus(_A)
class _FsTunlIfPmtuFlag_Type(TruthValue):defaultValue=2
_FsTunlIfPmtuFlag_Type.__name__=_F
_FsTunlIfPmtuFlag_Object=MibTableColumn
fsTunlIfPmtuFlag=_FsTunlIfPmtuFlag_Object((1,3,6,1,4,1,2076,95,1,1,1,1,18),_FsTunlIfPmtuFlag_Type())
fsTunlIfPmtuFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsTunlIfPmtuFlag.setStatus(_A)
_FsTunlIfStatus_Type=RowStatus
_FsTunlIfStatus_Object=MibTableColumn
fsTunlIfStatus=_FsTunlIfStatus_Object((1,3,6,1,4,1,2076,95,1,1,1,1,19),_FsTunlIfStatus_Type())
fsTunlIfStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsTunlIfStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'FsTunlType':FsTunlType,'FsIPv6FlowLabelOrAny':FsIPv6FlowLabelOrAny,'fsTunlMIB':fsTunlMIB,'fsTunlMIBObjects':fsTunlMIBObjects,'fsTunl':fsTunl,'fsTunlIfTable':fsTunlIfTable,'fsTunlIfEntry':fsTunlIfEntry,_J:fsTunlIfAddressType,_K:fsTunlIfLocalInetAddress,_L:fsTunlIfRemoteInetAddress,_M:fsTunlIfEncapsMethod,_N:fsTunlIfConfigID,'fsTunlIfHopLimit':fsTunlIfHopLimit,'fsTunlIfSecurity':fsTunlIfSecurity,'fsTunlIfTOS':fsTunlIfTOS,'fsTunlIfFlowLabel':fsTunlIfFlowLabel,'fsTunlIfMTU':fsTunlIfMTU,'fsTunlIfDirFlag':fsTunlIfDirFlag,'fsTunlIfDirection':fsTunlIfDirection,'fsTunlIfEncaplmt':fsTunlIfEncaplmt,'fsTunlIfEncapOption':fsTunlIfEncapOption,'fsTunlIfIndex':fsTunlIfIndex,'fsTunlIfAlias':fsTunlIfAlias,'fsTunlIfCksumFlag':fsTunlIfCksumFlag,'fsTunlIfPmtuFlag':fsTunlIfPmtuFlag,'fsTunlIfStatus':fsTunlIfStatus})