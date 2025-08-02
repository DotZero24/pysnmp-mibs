_L='rcRstpNewTopology'
_K='rcRstpDot1dStpTxHoldCount'
_J='2012-06-01 17:00'
_I='Integer32'
_H='rcRstpDot1dRstpBackupPorts'
_G='rcRstpDot1dRstpAlternatePorts'
_F='rcRstpDot1dStpBrokenPorts'
_E='rcRstpDot1dStpBlockedPorts'
_D='rcRstpDot1dStpForwardingPorts'
_C='read-only'
_B='current'
_A='RUGGEDCOM-STP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ruggedcomMgmt,ruggedcomTraps=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt','ruggedcomTraps')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rcRstp=ModuleIdentity((1,3,6,1,4,1,15004,4,5))
if mibBuilder.loadTexts:rcRstp.setRevisions((_J,_J,'2010-10-10 10:00'))
_RcRstpBase_ObjectIdentity=ObjectIdentity
rcRstpBase=_RcRstpBase_ObjectIdentity((1,3,6,1,4,1,15004,4,5,1))
class _RcRstpDot1dStpTxHoldCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,100))
_RcRstpDot1dStpTxHoldCount_Type.__name__=_I
_RcRstpDot1dStpTxHoldCount_Object=MibScalar
rcRstpDot1dStpTxHoldCount=_RcRstpDot1dStpTxHoldCount_Object((1,3,6,1,4,1,15004,4,5,1,1),_RcRstpDot1dStpTxHoldCount_Type())
rcRstpDot1dStpTxHoldCount.setMaxAccess('read-write')
if mibBuilder.loadTexts:rcRstpDot1dStpTxHoldCount.setStatus(_B)
_RcRstpDot1dStpForwardingPorts_Type=PortList
_RcRstpDot1dStpForwardingPorts_Object=MibScalar
rcRstpDot1dStpForwardingPorts=_RcRstpDot1dStpForwardingPorts_Object((1,3,6,1,4,1,15004,4,5,1,2),_RcRstpDot1dStpForwardingPorts_Type())
rcRstpDot1dStpForwardingPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpDot1dStpForwardingPorts.setStatus(_B)
_RcRstpDot1dStpBlockedPorts_Type=PortList
_RcRstpDot1dStpBlockedPorts_Object=MibScalar
rcRstpDot1dStpBlockedPorts=_RcRstpDot1dStpBlockedPorts_Object((1,3,6,1,4,1,15004,4,5,1,3),_RcRstpDot1dStpBlockedPorts_Type())
rcRstpDot1dStpBlockedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpDot1dStpBlockedPorts.setStatus(_B)
_RcRstpDot1dStpBrokenPorts_Type=PortList
_RcRstpDot1dStpBrokenPorts_Object=MibScalar
rcRstpDot1dStpBrokenPorts=_RcRstpDot1dStpBrokenPorts_Object((1,3,6,1,4,1,15004,4,5,1,4),_RcRstpDot1dStpBrokenPorts_Type())
rcRstpDot1dStpBrokenPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpDot1dStpBrokenPorts.setStatus(_B)
_RcRstpDot1dRstpAlternatePorts_Type=PortList
_RcRstpDot1dRstpAlternatePorts_Object=MibScalar
rcRstpDot1dRstpAlternatePorts=_RcRstpDot1dRstpAlternatePorts_Object((1,3,6,1,4,1,15004,4,5,1,5),_RcRstpDot1dRstpAlternatePorts_Type())
rcRstpDot1dRstpAlternatePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpDot1dRstpAlternatePorts.setStatus(_B)
_RcRstpDot1dRstpBackupPorts_Type=PortList
_RcRstpDot1dRstpBackupPorts_Object=MibScalar
rcRstpDot1dRstpBackupPorts=_RcRstpDot1dRstpBackupPorts_Object((1,3,6,1,4,1,15004,4,5,1,6),_RcRstpDot1dRstpBackupPorts_Type())
rcRstpDot1dRstpBackupPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcRstpDot1dRstpBackupPorts.setStatus(_B)
_RcRstpConformance_ObjectIdentity=ObjectIdentity
rcRstpConformance=_RcRstpConformance_ObjectIdentity((1,3,6,1,4,1,15004,4,5,3))
_RcRstpGroups_ObjectIdentity=ObjectIdentity
rcRstpGroups=_RcRstpGroups_ObjectIdentity((1,3,6,1,4,1,15004,4,5,3,2))
_RuggedcomRstpTraps_ObjectIdentity=ObjectIdentity
ruggedcomRstpTraps=_RuggedcomRstpTraps_ObjectIdentity((1,3,6,1,4,1,15004,5,11))
rcRstpBaseStpTxHoldCountGroup=ObjectGroup((1,3,6,1,4,1,15004,4,5,3,2,1))
rcRstpBaseStpTxHoldCountGroup.setObjects((_A,_K))
if mibBuilder.loadTexts:rcRstpBaseStpTxHoldCountGroup.setStatus(_B)
rcRstpBaseGroup=ObjectGroup((1,3,6,1,4,1,15004,4,5,3,2,2))
rcRstpBaseGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:rcRstpBaseGroup.setStatus(_B)
rcRstpNotifyGroup=ObjectGroup((1,3,6,1,4,1,15004,4,5,3,2,3))
rcRstpNotifyGroup.setObjects((_A,_L))
if mibBuilder.loadTexts:rcRstpNotifyGroup.setStatus(_B)
rcRstpNewTopology=NotificationType((1,3,6,1,4,1,15004,5,11,1))
rcRstpNewTopology.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,'dot1dStpRootPort'),(_A,'dot1dStpDesignatedRoot')))
if mibBuilder.loadTexts:rcRstpNewTopology.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rcRstp':rcRstp,'rcRstpBase':rcRstpBase,_K:rcRstpDot1dStpTxHoldCount,_D:rcRstpDot1dStpForwardingPorts,_E:rcRstpDot1dStpBlockedPorts,_F:rcRstpDot1dStpBrokenPorts,_G:rcRstpDot1dRstpAlternatePorts,_H:rcRstpDot1dRstpBackupPorts,'rcRstpConformance':rcRstpConformance,'rcRstpGroups':rcRstpGroups,'rcRstpBaseStpTxHoldCountGroup':rcRstpBaseStpTxHoldCountGroup,'rcRstpBaseGroup':rcRstpBaseGroup,'rcRstpNotifyGroup':rcRstpNotifyGroup,'ruggedcomRstpTraps':ruggedcomRstpTraps,_L:rcRstpNewTopology})