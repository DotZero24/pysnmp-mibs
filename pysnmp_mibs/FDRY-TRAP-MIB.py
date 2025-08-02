_I='SecurityLevel'
_H='SecurityModel'
_G='fdryTrapReceiverIndex'
_F='FDRY-TRAP-MIB'
_E='Integer32'
_D='InetAddressType'
_C='OctetString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fdryTrap,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','fdryTrap')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fdryTrapMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,10,1))
if mibBuilder.loadTexts:fdryTrapMIB.setRevisions(('2008-02-25 00:00','2023-05-25 00:00'))
class InetAddress(TextualConvention,OctetString):status=_A;displayHint='1x ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class SecurityModel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2c',2),('usm',3)))
class SecurityLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noAuth',1),('auth',2),('authPriv',3)))
_FdryTrapReceiver_ObjectIdentity=ObjectIdentity
fdryTrapReceiver=_FdryTrapReceiver_ObjectIdentity((1,3,6,1,4,1,1991,1,1,10,1,1))
_FdryTrapReceiverTable_Object=MibTable
fdryTrapReceiverTable=_FdryTrapReceiverTable_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1))
if mibBuilder.loadTexts:fdryTrapReceiverTable.setStatus(_A)
_FdryTrapReceiverEntry_Object=MibTableRow
fdryTrapReceiverEntry=_FdryTrapReceiverEntry_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1))
fdryTrapReceiverEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fdryTrapReceiverEntry.setStatus(_A)
_FdryTrapReceiverIndex_Type=Unsigned32
_FdryTrapReceiverIndex_Object=MibTableColumn
fdryTrapReceiverIndex=_FdryTrapReceiverIndex_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,1),_FdryTrapReceiverIndex_Type())
fdryTrapReceiverIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fdryTrapReceiverIndex.setStatus(_A)
class _FdryTrapReceiverAddrType_Type(InetAddressType):defaultValue=1
_FdryTrapReceiverAddrType_Type.__name__=_D
_FdryTrapReceiverAddrType_Object=MibTableColumn
fdryTrapReceiverAddrType=_FdryTrapReceiverAddrType_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,2),_FdryTrapReceiverAddrType_Type())
fdryTrapReceiverAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTrapReceiverAddrType.setStatus(_A)
_FdryTrapReceiverAddr_Type=InetAddress
_FdryTrapReceiverAddr_Object=MibTableColumn
fdryTrapReceiverAddr=_FdryTrapReceiverAddr_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,3),_FdryTrapReceiverAddr_Type())
fdryTrapReceiverAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTrapReceiverAddr.setStatus(_A)
class _FdryTrapReceiverCommunityOrSecurityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FdryTrapReceiverCommunityOrSecurityName_Type.__name__=_C
_FdryTrapReceiverCommunityOrSecurityName_Object=MibTableColumn
fdryTrapReceiverCommunityOrSecurityName=_FdryTrapReceiverCommunityOrSecurityName_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,4),_FdryTrapReceiverCommunityOrSecurityName_Type())
fdryTrapReceiverCommunityOrSecurityName.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTrapReceiverCommunityOrSecurityName.setStatus(_A)
class _FdryTrapReceiverUDPPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FdryTrapReceiverUDPPort_Type.__name__=_E
_FdryTrapReceiverUDPPort_Object=MibTableColumn
fdryTrapReceiverUDPPort=_FdryTrapReceiverUDPPort_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,5),_FdryTrapReceiverUDPPort_Type())
fdryTrapReceiverUDPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTrapReceiverUDPPort.setStatus(_A)
class _FdryTrapReceiverSecurityModel_Type(SecurityModel):defaultValue=1
_FdryTrapReceiverSecurityModel_Type.__name__=_H
_FdryTrapReceiverSecurityModel_Object=MibTableColumn
fdryTrapReceiverSecurityModel=_FdryTrapReceiverSecurityModel_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,6),_FdryTrapReceiverSecurityModel_Type())
fdryTrapReceiverSecurityModel.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTrapReceiverSecurityModel.setStatus(_A)
class _FdryTrapReceiverSecurityLevel_Type(SecurityLevel):defaultValue=1
_FdryTrapReceiverSecurityLevel_Type.__name__=_I
_FdryTrapReceiverSecurityLevel_Object=MibTableColumn
fdryTrapReceiverSecurityLevel=_FdryTrapReceiverSecurityLevel_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,7),_FdryTrapReceiverSecurityLevel_Type())
fdryTrapReceiverSecurityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTrapReceiverSecurityLevel.setStatus(_A)
_FdryTrapReceiverRowStatus_Type=RowStatus
_FdryTrapReceiverRowStatus_Object=MibTableColumn
fdryTrapReceiverRowStatus=_FdryTrapReceiverRowStatus_Object((1,3,6,1,4,1,1991,1,1,10,1,1,1,1,8),_FdryTrapReceiverRowStatus_Type())
fdryTrapReceiverRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fdryTrapReceiverRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'InetAddress':InetAddress,_H:SecurityModel,_I:SecurityLevel,'fdryTrapMIB':fdryTrapMIB,'fdryTrapReceiver':fdryTrapReceiver,'fdryTrapReceiverTable':fdryTrapReceiverTable,'fdryTrapReceiverEntry':fdryTrapReceiverEntry,_G:fdryTrapReceiverIndex,'fdryTrapReceiverAddrType':fdryTrapReceiverAddrType,'fdryTrapReceiverAddr':fdryTrapReceiverAddr,'fdryTrapReceiverCommunityOrSecurityName':fdryTrapReceiverCommunityOrSecurityName,'fdryTrapReceiverUDPPort':fdryTrapReceiverUDPPort,'fdryTrapReceiverSecurityModel':fdryTrapReceiverSecurityModel,'fdryTrapReceiverSecurityLevel':fdryTrapReceiverSecurityLevel,'fdryTrapReceiverRowStatus':fdryTrapReceiverRowStatus})