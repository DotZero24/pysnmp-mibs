_I='atLoopProtectRxLDFVlanId'
_H='atLoopProtectRxLDFIfIndex'
_G='Integer32'
_F='atLoopProtectAction'
_E='atLoopProtectVlanId'
_D='atLoopProtectIfIndex'
_C='read-only'
_B='current'
_A='AT-LOOPPROTECT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atLoopProtect=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,54))
if mibBuilder.loadTexts:atLoopProtect.setRevisions(('2008-08-12 00:00',))
_AtLoopProtectTrap_ObjectIdentity=ObjectIdentity
atLoopProtectTrap=_AtLoopProtectTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,54,0))
class _AtLoopProtectAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('atLoopProtectAction-LearnDisable',0),('atLoopProtectAction-LearnEnable',1),('atLoopProtectAction-PortDisable',2),('atLoopProtectAction-PortEnable',3),('atLoopProtectAction-LinkDown',4),('atLoopProtectAction-LinkUp',5),('atLoopProtectAction-VlanDisable',6),('atLoopProtectAction-VlanEnable',7)))
_AtLoopProtectAction_Type.__name__=_G
_AtLoopProtectAction_Object=MibScalar
atLoopProtectAction=_AtLoopProtectAction_Object((1,3,6,1,4,1,207,8,4,4,4,54,1),_AtLoopProtectAction_Type())
atLoopProtectAction.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:atLoopProtectAction.setStatus(_B)
_AtLoopProtectIfIndex_Type=InterfaceIndex
_AtLoopProtectIfIndex_Object=MibScalar
atLoopProtectIfIndex=_AtLoopProtectIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,54,2),_AtLoopProtectIfIndex_Type())
atLoopProtectIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atLoopProtectIfIndex.setStatus(_B)
_AtLoopProtectVlanId_Type=Integer32
_AtLoopProtectVlanId_Object=MibScalar
atLoopProtectVlanId=_AtLoopProtectVlanId_Object((1,3,6,1,4,1,207,8,4,4,4,54,3),_AtLoopProtectVlanId_Type())
atLoopProtectVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:atLoopProtectVlanId.setStatus(_B)
_AtLoopProtectRxLDFIfIndex_Type=InterfaceIndex
_AtLoopProtectRxLDFIfIndex_Object=MibScalar
atLoopProtectRxLDFIfIndex=_AtLoopProtectRxLDFIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,54,4),_AtLoopProtectRxLDFIfIndex_Type())
atLoopProtectRxLDFIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atLoopProtectRxLDFIfIndex.setStatus(_B)
_AtLoopProtectRxLDFVlanId_Type=Integer32
_AtLoopProtectRxLDFVlanId_Object=MibScalar
atLoopProtectRxLDFVlanId=_AtLoopProtectRxLDFVlanId_Object((1,3,6,1,4,1,207,8,4,4,4,54,5),_AtLoopProtectRxLDFVlanId_Type())
atLoopProtectRxLDFVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:atLoopProtectRxLDFVlanId.setStatus(_B)
atLoopProtectDetectedLoopBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,54,0,1))
atLoopProtectDetectedLoopBlockedTrap.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:atLoopProtectDetectedLoopBlockedTrap.setStatus(_B)
atLoopProtectRecoverLoopBlockedTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,54,0,2))
atLoopProtectRecoverLoopBlockedTrap.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:atLoopProtectRecoverLoopBlockedTrap.setStatus(_B)
atLoopProtectDetectedByLoopDetectionTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,54,0,3))
atLoopProtectDetectedByLoopDetectionTrap.setObjects(*((_A,_D),(_A,_E),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:atLoopProtectDetectedByLoopDetectionTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'atLoopProtect':atLoopProtect,'atLoopProtectTrap':atLoopProtectTrap,'atLoopProtectDetectedLoopBlockedTrap':atLoopProtectDetectedLoopBlockedTrap,'atLoopProtectRecoverLoopBlockedTrap':atLoopProtectRecoverLoopBlockedTrap,'atLoopProtectDetectedByLoopDetectionTrap':atLoopProtectDetectedByLoopDetectionTrap,_F:atLoopProtectAction,_D:atLoopProtectIfIndex,_E:atLoopProtectVlanId,_H:atLoopProtectRxLDFIfIndex,_I:atLoopProtectRxLDFVlanId})