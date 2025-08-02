_J='mitelNatGrpRedirOldPort'
_I='mitelNatGrpRedirProto'
_H='mitelNatGrpRedirOldAddr'
_G='read-create'
_F='mitelNatGrpIfAddr'
_E='read-only'
_D='MITEL-NAT-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
mitelIpGrpNatGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,1,2))
if mibBuilder.loadTexts:mitelIpGrpNatGroup.setRevisions(('2003-03-24 10:01','1999-03-01 00:00'))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
_MitelRouterIpGroup_ObjectIdentity=ObjectIdentity
mitelRouterIpGroup=_MitelRouterIpGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,1))
_MitelNatGrpIfTable_Object=MibTable
mitelNatGrpIfTable=_MitelNatGrpIfTable_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1))
if mibBuilder.loadTexts:mitelNatGrpIfTable.setStatus(_A)
_MitelNatGrpIfEntry_Object=MibTableRow
mitelNatGrpIfEntry=_MitelNatGrpIfEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1))
mitelNatGrpIfEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:mitelNatGrpIfEntry.setStatus(_A)
_MitelNatGrpIfAddr_Type=IpAddress
_MitelNatGrpIfAddr_Object=MibTableColumn
mitelNatGrpIfAddr=_MitelNatGrpIfAddr_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,1),_MitelNatGrpIfAddr_Type())
mitelNatGrpIfAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelNatGrpIfAddr.setStatus(_A)
class _MitelNatGrpIfEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MitelNatGrpIfEnable_Type.__name__=_B
_MitelNatGrpIfEnable_Object=MibTableColumn
mitelNatGrpIfEnable=_MitelNatGrpIfEnable_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,2),_MitelNatGrpIfEnable_Type())
mitelNatGrpIfEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpIfEnable.setStatus(_A)
class _MitelNatGrpIfUdpLifetime_Type(Integer32):defaultValue=900
_MitelNatGrpIfUdpLifetime_Type.__name__=_B
_MitelNatGrpIfUdpLifetime_Object=MibTableColumn
mitelNatGrpIfUdpLifetime=_MitelNatGrpIfUdpLifetime_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,3),_MitelNatGrpIfUdpLifetime_Type())
mitelNatGrpIfUdpLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpIfUdpLifetime.setStatus(_A)
class _MitelNatGrpIfTcpLifetime_Type(Integer32):defaultValue=900
_MitelNatGrpIfTcpLifetime_Type.__name__=_B
_MitelNatGrpIfTcpLifetime_Object=MibTableColumn
mitelNatGrpIfTcpLifetime=_MitelNatGrpIfTcpLifetime_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,4),_MitelNatGrpIfTcpLifetime_Type())
mitelNatGrpIfTcpLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpIfTcpLifetime.setStatus(_A)
class _MitelNatGrpIfTcpFinLifetime_Type(Integer32):defaultValue=120
_MitelNatGrpIfTcpFinLifetime_Type.__name__=_B
_MitelNatGrpIfTcpFinLifetime_Object=MibTableColumn
mitelNatGrpIfTcpFinLifetime=_MitelNatGrpIfTcpFinLifetime_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,5),_MitelNatGrpIfTcpFinLifetime_Type())
mitelNatGrpIfTcpFinLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpIfTcpFinLifetime.setStatus(_A)
class _MitelNatGrpIfTcpRstLifetime_Type(Integer32):defaultValue=120
_MitelNatGrpIfTcpRstLifetime_Type.__name__=_B
_MitelNatGrpIfTcpRstLifetime_Object=MibTableColumn
mitelNatGrpIfTcpRstLifetime=_MitelNatGrpIfTcpRstLifetime_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,6),_MitelNatGrpIfTcpRstLifetime_Type())
mitelNatGrpIfTcpRstLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpIfTcpRstLifetime.setStatus(_A)
class _MitelNatGrpIfPingLifetime_Type(Integer32):defaultValue=120
_MitelNatGrpIfPingLifetime_Type.__name__=_B
_MitelNatGrpIfPingLifetime_Object=MibTableColumn
mitelNatGrpIfPingLifetime=_MitelNatGrpIfPingLifetime_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,7),_MitelNatGrpIfPingLifetime_Type())
mitelNatGrpIfPingLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpIfPingLifetime.setStatus(_A)
_MitelNatGrpIfStatus_Type=RowStatus
_MitelNatGrpIfStatus_Object=MibTableColumn
mitelNatGrpIfStatus=_MitelNatGrpIfStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,8),_MitelNatGrpIfStatus_Type())
mitelNatGrpIfStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:mitelNatGrpIfStatus.setStatus(_A)
_MitelNatGrpIfIndex_Type=Integer32
_MitelNatGrpIfIndex_Object=MibTableColumn
mitelNatGrpIfIndex=_MitelNatGrpIfIndex_Object((1,3,6,1,4,1,1027,4,8,1,1,2,1,1,9),_MitelNatGrpIfIndex_Type())
mitelNatGrpIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelNatGrpIfIndex.setStatus(_A)
_MitelNatGrpRedirTable_Object=MibTable
mitelNatGrpRedirTable=_MitelNatGrpRedirTable_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2))
if mibBuilder.loadTexts:mitelNatGrpRedirTable.setStatus(_A)
_MitelNatGrpRedirEntry_Object=MibTableRow
mitelNatGrpRedirEntry=_MitelNatGrpRedirEntry_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2,1))
mitelNatGrpRedirEntry.setIndexNames((0,_D,_H),(0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:mitelNatGrpRedirEntry.setStatus(_A)
_MitelNatGrpRedirOldAddr_Type=IpAddress
_MitelNatGrpRedirOldAddr_Object=MibTableColumn
mitelNatGrpRedirOldAddr=_MitelNatGrpRedirOldAddr_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2,1,1),_MitelNatGrpRedirOldAddr_Type())
mitelNatGrpRedirOldAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelNatGrpRedirOldAddr.setStatus(_A)
_MitelNatGrpRedirProto_Type=Integer32
_MitelNatGrpRedirProto_Object=MibTableColumn
mitelNatGrpRedirProto=_MitelNatGrpRedirProto_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2,1,2),_MitelNatGrpRedirProto_Type())
mitelNatGrpRedirProto.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelNatGrpRedirProto.setStatus(_A)
_MitelNatGrpRedirOldPort_Type=Integer32
_MitelNatGrpRedirOldPort_Object=MibTableColumn
mitelNatGrpRedirOldPort=_MitelNatGrpRedirOldPort_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2,1,3),_MitelNatGrpRedirOldPort_Type())
mitelNatGrpRedirOldPort.setMaxAccess(_E)
if mibBuilder.loadTexts:mitelNatGrpRedirOldPort.setStatus(_A)
_MitelNatGrpRedirNewAddr_Type=IpAddress
_MitelNatGrpRedirNewAddr_Object=MibTableColumn
mitelNatGrpRedirNewAddr=_MitelNatGrpRedirNewAddr_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2,1,4),_MitelNatGrpRedirNewAddr_Type())
mitelNatGrpRedirNewAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpRedirNewAddr.setStatus(_A)
class _MitelNatGrpRedirNewPort_Type(Integer32):defaultValue=0
_MitelNatGrpRedirNewPort_Type.__name__=_B
_MitelNatGrpRedirNewPort_Object=MibTableColumn
mitelNatGrpRedirNewPort=_MitelNatGrpRedirNewPort_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2,1,5),_MitelNatGrpRedirNewPort_Type())
mitelNatGrpRedirNewPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelNatGrpRedirNewPort.setStatus(_A)
_MitelNatGrpRedirStatus_Type=RowStatus
_MitelNatGrpRedirStatus_Object=MibTableColumn
mitelNatGrpRedirStatus=_MitelNatGrpRedirStatus_Object((1,3,6,1,4,1,1027,4,8,1,1,2,2,1,6),_MitelNatGrpRedirStatus_Type())
mitelNatGrpRedirStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:mitelNatGrpRedirStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mitel':mitel,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterIpGroup':mitelRouterIpGroup,'mitelIpGrpNatGroup':mitelIpGrpNatGroup,'mitelNatGrpIfTable':mitelNatGrpIfTable,'mitelNatGrpIfEntry':mitelNatGrpIfEntry,_F:mitelNatGrpIfAddr,'mitelNatGrpIfEnable':mitelNatGrpIfEnable,'mitelNatGrpIfUdpLifetime':mitelNatGrpIfUdpLifetime,'mitelNatGrpIfTcpLifetime':mitelNatGrpIfTcpLifetime,'mitelNatGrpIfTcpFinLifetime':mitelNatGrpIfTcpFinLifetime,'mitelNatGrpIfTcpRstLifetime':mitelNatGrpIfTcpRstLifetime,'mitelNatGrpIfPingLifetime':mitelNatGrpIfPingLifetime,'mitelNatGrpIfStatus':mitelNatGrpIfStatus,'mitelNatGrpIfIndex':mitelNatGrpIfIndex,'mitelNatGrpRedirTable':mitelNatGrpRedirTable,'mitelNatGrpRedirEntry':mitelNatGrpRedirEntry,_H:mitelNatGrpRedirOldAddr,_I:mitelNatGrpRedirProto,_J:mitelNatGrpRedirOldPort,'mitelNatGrpRedirNewAddr':mitelNatGrpRedirNewAddr,'mitelNatGrpRedirNewPort':mitelNatGrpRedirNewPort,'mitelNatGrpRedirStatus':mitelNatGrpRedirStatus})