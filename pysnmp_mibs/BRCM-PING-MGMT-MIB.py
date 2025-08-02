_J='milliseconds'
_I='InetAddressType'
_H='InetAddress'
_G='bytes'
_F='TruthValue'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataMgmtBase,=mibBuilder.importSymbols('BRCM-CABLEDATA-MGMT-MIB','cableDataMgmtBase')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
pingMgmt=ModuleIdentity((1,3,6,1,4,1,4413,2,2,2,1,1,5))
if mibBuilder.loadTexts:pingMgmt.setRevisions(('2007-02-05 00:00','2006-06-15 00:00'))
class _PingTargetAddressType_Type(InetAddressType):defaultValue=1
_PingTargetAddressType_Type.__name__=_I
_PingTargetAddressType_Object=MibScalar
pingTargetAddressType=_PingTargetAddressType_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,1),_PingTargetAddressType_Type())
pingTargetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:pingTargetAddressType.setStatus(_A)
class _PingTargetAddress_Type(InetAddress):defaultHexValue='00000000'
_PingTargetAddress_Type.__name__=_H
_PingTargetAddress_Object=MibScalar
pingTargetAddress=_PingTargetAddress_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,2),_PingTargetAddress_Type())
pingTargetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pingTargetAddress.setStatus(_A)
class _PingNumPkts_Type(Unsigned32):defaultValue=3
_PingNumPkts_Type.__name__=_D
_PingNumPkts_Object=MibScalar
pingNumPkts=_PingNumPkts_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,3),_PingNumPkts_Type())
pingNumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:pingNumPkts.setStatus(_A)
class _PingPktStartSize_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_PingPktStartSize_Type.__name__=_D
_PingPktStartSize_Object=MibScalar
pingPktStartSize=_PingPktStartSize_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,4),_PingPktStartSize_Type())
pingPktStartSize.setMaxAccess(_B)
if mibBuilder.loadTexts:pingPktStartSize.setStatus(_A)
if mibBuilder.loadTexts:pingPktStartSize.setUnits(_G)
class _PingPktEndSize_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_PingPktEndSize_Type.__name__=_D
_PingPktEndSize_Object=MibScalar
pingPktEndSize=_PingPktEndSize_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,5),_PingPktEndSize_Type())
pingPktEndSize.setMaxAccess(_B)
if mibBuilder.loadTexts:pingPktEndSize.setStatus(_A)
if mibBuilder.loadTexts:pingPktEndSize.setUnits(_G)
class _PingPktStepSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1454,1454))
_PingPktStepSize_Type.__name__=_E
_PingPktStepSize_Object=MibScalar
pingPktStepSize=_PingPktStepSize_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,6),_PingPktStepSize_Type())
pingPktStepSize.setMaxAccess(_B)
if mibBuilder.loadTexts:pingPktStepSize.setStatus(_A)
if mibBuilder.loadTexts:pingPktStepSize.setUnits(_G)
class _PingInterval_Type(Unsigned32):defaultValue=0
_PingInterval_Type.__name__=_D
_PingInterval_Object=MibScalar
pingInterval=_PingInterval_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,7),_PingInterval_Type())
pingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:pingInterval.setStatus(_A)
if mibBuilder.loadTexts:pingInterval.setUnits(_J)
class _PingTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_PingTimeout_Type.__name__=_E
_PingTimeout_Object=MibScalar
pingTimeout=_PingTimeout_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,8),_PingTimeout_Type())
pingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:pingTimeout.setStatus(_A)
if mibBuilder.loadTexts:pingTimeout.setUnits(_J)
class _PingVerifyReply_Type(TruthValue):defaultValue=1
_PingVerifyReply_Type.__name__=_F
_PingVerifyReply_Object=MibScalar
pingVerifyReply=_PingVerifyReply_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,9),_PingVerifyReply_Type())
pingVerifyReply.setMaxAccess(_B)
if mibBuilder.loadTexts:pingVerifyReply.setStatus(_A)
class _PingIpStackNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PingIpStackNumber_Type.__name__=_E
_PingIpStackNumber_Object=MibScalar
pingIpStackNumber=_PingIpStackNumber_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,10),_PingIpStackNumber_Type())
pingIpStackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pingIpStackNumber.setStatus(_A)
class _PingNow_Type(TruthValue):defaultValue=1
_PingNow_Type.__name__=_F
_PingNow_Object=MibScalar
pingNow=_PingNow_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,11),_PingNow_Type())
pingNow.setMaxAccess(_B)
if mibBuilder.loadTexts:pingNow.setStatus(_A)
_PingPktsSent_Type=Counter32
_PingPktsSent_Object=MibScalar
pingPktsSent=_PingPktsSent_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,12),_PingPktsSent_Type())
pingPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:pingPktsSent.setStatus(_A)
_PingRepliesReceived_Type=Counter32
_PingRepliesReceived_Object=MibScalar
pingRepliesReceived=_PingRepliesReceived_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,13),_PingRepliesReceived_Type())
pingRepliesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pingRepliesReceived.setStatus(_A)
_PingRepliesVerified_Type=Counter32
_PingRepliesVerified_Object=MibScalar
pingRepliesVerified=_PingRepliesVerified_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,14),_PingRepliesVerified_Type())
pingRepliesVerified.setMaxAccess(_C)
if mibBuilder.loadTexts:pingRepliesVerified.setStatus(_A)
_PingOctetsSent_Type=Counter32
_PingOctetsSent_Object=MibScalar
pingOctetsSent=_PingOctetsSent_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,15),_PingOctetsSent_Type())
pingOctetsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:pingOctetsSent.setStatus(_A)
_PingOctetsReceived_Type=Counter32
_PingOctetsReceived_Object=MibScalar
pingOctetsReceived=_PingOctetsReceived_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,16),_PingOctetsReceived_Type())
pingOctetsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pingOctetsReceived.setStatus(_A)
_PingIcmpErrors_Type=Counter32
_PingIcmpErrors_Object=MibScalar
pingIcmpErrors=_PingIcmpErrors_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,17),_PingIcmpErrors_Type())
pingIcmpErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pingIcmpErrors.setStatus(_A)
_PingLastIcmpError_Type=Unsigned32
_PingLastIcmpError_Object=MibScalar
pingLastIcmpError=_PingLastIcmpError_Object((1,3,6,1,4,1,4413,2,2,2,1,1,5,18),_PingLastIcmpError_Type())
pingLastIcmpError.setMaxAccess(_C)
if mibBuilder.loadTexts:pingLastIcmpError.setStatus(_A)
mibBuilder.exportSymbols('BRCM-PING-MGMT-MIB',**{'pingMgmt':pingMgmt,'pingTargetAddressType':pingTargetAddressType,'pingTargetAddress':pingTargetAddress,'pingNumPkts':pingNumPkts,'pingPktStartSize':pingPktStartSize,'pingPktEndSize':pingPktEndSize,'pingPktStepSize':pingPktStepSize,'pingInterval':pingInterval,'pingTimeout':pingTimeout,'pingVerifyReply':pingVerifyReply,'pingIpStackNumber':pingIpStackNumber,'pingNow':pingNow,'pingPktsSent':pingPktsSent,'pingRepliesReceived':pingRepliesReceived,'pingRepliesVerified':pingRepliesVerified,'pingOctetsSent':pingOctetsSent,'pingOctetsReceived':pingOctetsReceived,'pingIcmpErrors':pingIcmpErrors,'pingLastIcmpError':pingLastIcmpError})