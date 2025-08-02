_F='dpTrafficSegIfCfgGroup'
_E='dpTrafficSegForwardPorts'
_D='ifIndex'
_C='IF-MIB'
_B='DLINKPRIME-TRAFFIC-SEGMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_C,'InterfaceIndex',_D)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dlinkPrimeTrafficSegMIB=ModuleIdentity((1,3,6,1,4,1,171,15,25))
if mibBuilder.loadTexts:dlinkPrimeTrafficSegMIB.setRevisions(('2014-04-26 00:00',))
_DpTrafficSegNotifications_ObjectIdentity=ObjectIdentity
dpTrafficSegNotifications=_DpTrafficSegNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,25,0))
_DpTrafficSegObjects_ObjectIdentity=ObjectIdentity
dpTrafficSegObjects=_DpTrafficSegObjects_ObjectIdentity((1,3,6,1,4,1,171,15,25,1))
_DpTrafficSegForwardDomainTable_Object=MibTable
dpTrafficSegForwardDomainTable=_DpTrafficSegForwardDomainTable_Object((1,3,6,1,4,1,171,15,25,1,1))
if mibBuilder.loadTexts:dpTrafficSegForwardDomainTable.setStatus(_A)
_DpTrafficSegForwardDomainEntry_Object=MibTableRow
dpTrafficSegForwardDomainEntry=_DpTrafficSegForwardDomainEntry_Object((1,3,6,1,4,1,171,15,25,1,1,1))
dpTrafficSegForwardDomainEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dpTrafficSegForwardDomainEntry.setStatus(_A)
_DpTrafficSegForwardPorts_Type=PortList
_DpTrafficSegForwardPorts_Object=MibTableColumn
dpTrafficSegForwardPorts=_DpTrafficSegForwardPorts_Object((1,3,6,1,4,1,171,15,25,1,1,1,1),_DpTrafficSegForwardPorts_Type())
dpTrafficSegForwardPorts.setMaxAccess('read-write')
if mibBuilder.loadTexts:dpTrafficSegForwardPorts.setStatus(_A)
_DpTrafficSegConformance_ObjectIdentity=ObjectIdentity
dpTrafficSegConformance=_DpTrafficSegConformance_ObjectIdentity((1,3,6,1,4,1,171,15,25,2))
_DpTrafficSegMIBCompliances_ObjectIdentity=ObjectIdentity
dpTrafficSegMIBCompliances=_DpTrafficSegMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,25,2,1))
_DpTrafficSegMIBGroups_ObjectIdentity=ObjectIdentity
dpTrafficSegMIBGroups=_DpTrafficSegMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,25,2,2))
dpTrafficSegIfCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,25,2,2,1))
dpTrafficSegIfCfgGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:dpTrafficSegIfCfgGroup.setStatus(_A)
dpTrafficSegMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,25,2,1,1))
dpTrafficSegMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:dpTrafficSegMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeTrafficSegMIB':dlinkPrimeTrafficSegMIB,'dpTrafficSegNotifications':dpTrafficSegNotifications,'dpTrafficSegObjects':dpTrafficSegObjects,'dpTrafficSegForwardDomainTable':dpTrafficSegForwardDomainTable,'dpTrafficSegForwardDomainEntry':dpTrafficSegForwardDomainEntry,_E:dpTrafficSegForwardPorts,'dpTrafficSegConformance':dpTrafficSegConformance,'dpTrafficSegMIBCompliances':dpTrafficSegMIBCompliances,'dpTrafficSegMIBCompliance':dpTrafficSegMIBCompliance,'dpTrafficSegMIBGroups':dpTrafficSegMIBGroups,_F:dpTrafficSegIfCfgGroup})