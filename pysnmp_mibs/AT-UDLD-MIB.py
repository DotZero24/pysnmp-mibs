_C='atUdldIfIndex'
_B='AT-UDLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atUdld=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,550))
if mibBuilder.loadTexts:atUdld.setRevisions(('2011-11-22 00:00','2011-05-15 00:00'))
_AtUdldTrap_ObjectIdentity=ObjectIdentity
atUdldTrap=_AtUdldTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,550,0))
_AtUdldIfIndex_Type=InterfaceIndex
_AtUdldIfIndex_Object=MibScalar
atUdldIfIndex=_AtUdldIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,550,1),_AtUdldIfIndex_Type())
atUdldIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:atUdldIfIndex.setStatus(_A)
atUdldPortDisabledTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,550,0,1))
atUdldPortDisabledTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:atUdldPortDisabledTrap.setStatus(_A)
atUdldPortRecoveredTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,550,0,2))
atUdldPortRecoveredTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:atUdldPortRecoveredTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atUdld':atUdld,'atUdldTrap':atUdldTrap,'atUdldPortDisabledTrap':atUdldPortDisabledTrap,'atUdldPortRecoveredTrap':atUdldPortRecoveredTrap,_C:atUdldIfIndex})