_E='atQosv2VlanId'
_D='atQosv2IfIndex'
_C='read-only'
_B='AT-QOSv2-MIB'
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
atQosv2=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,503))
if mibBuilder.loadTexts:atQosv2.setRevisions(('2015-08-31 00:00',))
_AtQosv2Notification_ObjectIdentity=ObjectIdentity
atQosv2Notification=_AtQosv2Notification_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,503,0))
_AtQosv2NotificationVariables_ObjectIdentity=ObjectIdentity
atQosv2NotificationVariables=_AtQosv2NotificationVariables_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,503,1))
_AtQosv2IfIndex_Type=InterfaceIndex
_AtQosv2IfIndex_Object=MibScalar
atQosv2IfIndex=_AtQosv2IfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,503,1,1),_AtQosv2IfIndex_Type())
atQosv2IfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:atQosv2IfIndex.setStatus(_A)
_AtQosv2VlanId_Type=Integer32
_AtQosv2VlanId_Object=MibScalar
atQosv2VlanId=_AtQosv2VlanId_Object((1,3,6,1,4,1,207,8,4,4,4,503,1,2),_AtQosv2VlanId_Type())
atQosv2VlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:atQosv2VlanId.setStatus(_A)
atQosv2StormDetectionTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,503,0,1))
atQosv2StormDetectionTrap.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:atQosv2StormDetectionTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'atQosv2':atQosv2,'atQosv2Notification':atQosv2Notification,'atQosv2StormDetectionTrap':atQosv2StormDetectionTrap,'atQosv2NotificationVariables':atQosv2NotificationVariables,_D:atQosv2IfIndex,_E:atQosv2VlanId})