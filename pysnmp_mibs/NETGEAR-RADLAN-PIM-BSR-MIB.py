_K='seconds'
_J='not-accessible'
_I='rlPimBsrCandidateRPAddress'
_H='rlPimBsrCandidateRPAddressType'
_G='TruthValue'
_F='DisplayString'
_E='InetAddress'
_D='NETGEAR-RADLAN-PIM-BSR-MIB'
_C='Unsigned32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetVersion=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,'InetAddressPrefixLength','InetAddressType','InetVersion')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention',_G)
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminStatusUp',1),('adminStatusDown',2)))
class OperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
_RlPimBsrCandidateRPTable_Object=MibTable
rlPimBsrCandidateRPTable=_RlPimBsrCandidateRPTable_Object((1,3,6,1,4,1,4526,17,220))
if mibBuilder.loadTexts:rlPimBsrCandidateRPTable.setStatus(_A)
_RlPimBsrCandidateRPEntry_Object=MibTableRow
rlPimBsrCandidateRPEntry=_RlPimBsrCandidateRPEntry_Object((1,3,6,1,4,1,4526,17,220,1))
rlPimBsrCandidateRPEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:rlPimBsrCandidateRPEntry.setStatus(_A)
_RlPimBsrCandidateRPAddressType_Type=InetAddressType
_RlPimBsrCandidateRPAddressType_Object=MibTableColumn
rlPimBsrCandidateRPAddressType=_RlPimBsrCandidateRPAddressType_Object((1,3,6,1,4,1,4526,17,220,1,1),_RlPimBsrCandidateRPAddressType_Type())
rlPimBsrCandidateRPAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:rlPimBsrCandidateRPAddressType.setStatus(_A)
class _RlPimBsrCandidateRPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16))
_RlPimBsrCandidateRPAddress_Type.__name__=_E
_RlPimBsrCandidateRPAddress_Object=MibTableColumn
rlPimBsrCandidateRPAddress=_RlPimBsrCandidateRPAddress_Object((1,3,6,1,4,1,4526,17,220,1,2),_RlPimBsrCandidateRPAddress_Type())
rlPimBsrCandidateRPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:rlPimBsrCandidateRPAddress.setStatus(_A)
class _RlPimBsrCandidateRPGroupPrefixList_Type(DisplayString):defaultValue=OctetString('')
_RlPimBsrCandidateRPGroupPrefixList_Type.__name__=_F
_RlPimBsrCandidateRPGroupPrefixList_Object=MibTableColumn
rlPimBsrCandidateRPGroupPrefixList=_RlPimBsrCandidateRPGroupPrefixList_Object((1,3,6,1,4,1,4526,17,220,1,3),_RlPimBsrCandidateRPGroupPrefixList_Type())
rlPimBsrCandidateRPGroupPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimBsrCandidateRPGroupPrefixList.setStatus(_A)
class _RlPimBsrCandidateRPBidir_Type(TruthValue):defaultValue=2
_RlPimBsrCandidateRPBidir_Type.__name__=_G
_RlPimBsrCandidateRPBidir_Object=MibTableColumn
rlPimBsrCandidateRPBidir=_RlPimBsrCandidateRPBidir_Object((1,3,6,1,4,1,4526,17,220,1,5),_RlPimBsrCandidateRPBidir_Type())
rlPimBsrCandidateRPBidir.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimBsrCandidateRPBidir.setStatus(_A)
_RlPimBsrCandidateRPAdvTimer_Type=TimeTicks
_RlPimBsrCandidateRPAdvTimer_Object=MibTableColumn
rlPimBsrCandidateRPAdvTimer=_RlPimBsrCandidateRPAdvTimer_Object((1,3,6,1,4,1,4526,17,220,1,6),_RlPimBsrCandidateRPAdvTimer_Type())
rlPimBsrCandidateRPAdvTimer.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlPimBsrCandidateRPAdvTimer.setStatus(_A)
class _RlPimBsrCandidateRPPriority_Type(Unsigned32):defaultValue=192;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlPimBsrCandidateRPPriority_Type.__name__=_C
_RlPimBsrCandidateRPPriority_Object=MibTableColumn
rlPimBsrCandidateRPPriority=_RlPimBsrCandidateRPPriority_Object((1,3,6,1,4,1,4526,17,220,1,7),_RlPimBsrCandidateRPPriority_Type())
rlPimBsrCandidateRPPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimBsrCandidateRPPriority.setStatus(_A)
class _RlPimBsrCandidateRPAdvInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26214))
_RlPimBsrCandidateRPAdvInterval_Type.__name__=_C
_RlPimBsrCandidateRPAdvInterval_Object=MibTableColumn
rlPimBsrCandidateRPAdvInterval=_RlPimBsrCandidateRPAdvInterval_Object((1,3,6,1,4,1,4526,17,220,1,8),_RlPimBsrCandidateRPAdvInterval_Type())
rlPimBsrCandidateRPAdvInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimBsrCandidateRPAdvInterval.setStatus(_A)
if mibBuilder.loadTexts:rlPimBsrCandidateRPAdvInterval.setUnits(_K)
class _RlPimBsrCandidateRPHoldtime_Type(Unsigned32):defaultValue=150;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPimBsrCandidateRPHoldtime_Type.__name__=_C
_RlPimBsrCandidateRPHoldtime_Object=MibTableColumn
rlPimBsrCandidateRPHoldtime=_RlPimBsrCandidateRPHoldtime_Object((1,3,6,1,4,1,4526,17,220,1,9),_RlPimBsrCandidateRPHoldtime_Type())
rlPimBsrCandidateRPHoldtime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimBsrCandidateRPHoldtime.setStatus(_A)
if mibBuilder.loadTexts:rlPimBsrCandidateRPHoldtime.setUnits(_K)
_RlPimBsrCandidateRPStatus_Type=RowStatus
_RlPimBsrCandidateRPStatus_Object=MibTableColumn
rlPimBsrCandidateRPStatus=_RlPimBsrCandidateRPStatus_Object((1,3,6,1,4,1,4526,17,220,1,10),_RlPimBsrCandidateRPStatus_Type())
rlPimBsrCandidateRPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimBsrCandidateRPStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'AdminStatus':AdminStatus,'OperStatus':OperStatus,'rlPimBsrCandidateRPTable':rlPimBsrCandidateRPTable,'rlPimBsrCandidateRPEntry':rlPimBsrCandidateRPEntry,_H:rlPimBsrCandidateRPAddressType,_I:rlPimBsrCandidateRPAddress,'rlPimBsrCandidateRPGroupPrefixList':rlPimBsrCandidateRPGroupPrefixList,'rlPimBsrCandidateRPBidir':rlPimBsrCandidateRPBidir,'rlPimBsrCandidateRPAdvTimer':rlPimBsrCandidateRPAdvTimer,'rlPimBsrCandidateRPPriority':rlPimBsrCandidateRPPriority,'rlPimBsrCandidateRPAdvInterval':rlPimBsrCandidateRPAdvInterval,'rlPimBsrCandidateRPHoldtime':rlPimBsrCandidateRPHoldtime,'rlPimBsrCandidateRPStatus':rlPimBsrCandidateRPStatus})