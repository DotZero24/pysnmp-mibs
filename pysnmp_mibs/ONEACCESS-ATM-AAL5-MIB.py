_I='oacExpIMAtmAal5GeneralGroup'
_H='oacExpIMAtmAal5VclLogicalIndexIfIndex'
_G='ifIndex'
_F='IF-MIB'
_E='atmVclVpi'
_D='atmVclVci'
_C='ONEACCESS-ATM-AAL5-MIB'
_B='ATM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclVci,atmVclVpi=mibBuilder.importSymbols(_B,_D,_E)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
oacExpIMAtmAal5,oacMIBModules,oacRequirements=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMAtmAal5','oacMIBModules','oacRequirements')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacAtmAal5MIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,800))
if mibBuilder.loadTexts:oacAtmAal5MIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 10:00'))
_OacExpIMAtmAal5Conformance_ObjectIdentity=ObjectIdentity
oacExpIMAtmAal5Conformance=_OacExpIMAtmAal5Conformance_ObjectIdentity((1,3,6,1,4,1,13191,5,800))
_OacExpIMAtmAal5Groups_ObjectIdentity=ObjectIdentity
oacExpIMAtmAal5Groups=_OacExpIMAtmAal5Groups_ObjectIdentity((1,3,6,1,4,1,13191,5,800,1))
_OacExpIMAtmAal5Compliances_ObjectIdentity=ObjectIdentity
oacExpIMAtmAal5Compliances=_OacExpIMAtmAal5Compliances_ObjectIdentity((1,3,6,1,4,1,13191,5,800,2))
_OacExpIMAtmAal5Objects_ObjectIdentity=ObjectIdentity
oacExpIMAtmAal5Objects=_OacExpIMAtmAal5Objects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,3,1))
_OacExpIMAtmAal5VclLogicalIndexTable_Object=MibTable
oacExpIMAtmAal5VclLogicalIndexTable=_OacExpIMAtmAal5VclLogicalIndexTable_Object((1,3,6,1,4,1,13191,10,3,2,3,1,1))
if mibBuilder.loadTexts:oacExpIMAtmAal5VclLogicalIndexTable.setStatus(_A)
_OacExpIMAtmAal5VclLogicalIndexEntry_Object=MibTableRow
oacExpIMAtmAal5VclLogicalIndexEntry=_OacExpIMAtmAal5VclLogicalIndexEntry_Object((1,3,6,1,4,1,13191,10,3,2,3,1,1,1))
oacExpIMAtmAal5VclLogicalIndexEntry.setIndexNames((0,_F,_G),(0,_B,_E),(0,_B,_D))
if mibBuilder.loadTexts:oacExpIMAtmAal5VclLogicalIndexEntry.setStatus(_A)
_OacExpIMAtmAal5VclLogicalIndexIfIndex_Type=InterfaceIndex
_OacExpIMAtmAal5VclLogicalIndexIfIndex_Object=MibTableColumn
oacExpIMAtmAal5VclLogicalIndexIfIndex=_OacExpIMAtmAal5VclLogicalIndexIfIndex_Object((1,3,6,1,4,1,13191,10,3,2,3,1,1,1,1),_OacExpIMAtmAal5VclLogicalIndexIfIndex_Type())
oacExpIMAtmAal5VclLogicalIndexIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:oacExpIMAtmAal5VclLogicalIndexIfIndex.setStatus(_A)
_OacExpIMAtmAal5Notifications_ObjectIdentity=ObjectIdentity
oacExpIMAtmAal5Notifications=_OacExpIMAtmAal5Notifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,3,2))
oacExpIMAtmAal5GeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,5,800,1,1))
oacExpIMAtmAal5GeneralGroup.setObjects((_C,_H))
if mibBuilder.loadTexts:oacExpIMAtmAal5GeneralGroup.setStatus(_A)
oacExpIMAtmAal5Compliance=ModuleCompliance((1,3,6,1,4,1,13191,5,800,2,1))
oacExpIMAtmAal5Compliance.setObjects((_C,_I))
if mibBuilder.loadTexts:oacExpIMAtmAal5Compliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'oacAtmAal5MIBModule':oacAtmAal5MIBModule,'oacExpIMAtmAal5Conformance':oacExpIMAtmAal5Conformance,'oacExpIMAtmAal5Groups':oacExpIMAtmAal5Groups,_I:oacExpIMAtmAal5GeneralGroup,'oacExpIMAtmAal5Compliances':oacExpIMAtmAal5Compliances,'oacExpIMAtmAal5Compliance':oacExpIMAtmAal5Compliance,'oacExpIMAtmAal5Objects':oacExpIMAtmAal5Objects,'oacExpIMAtmAal5VclLogicalIndexTable':oacExpIMAtmAal5VclLogicalIndexTable,'oacExpIMAtmAal5VclLogicalIndexEntry':oacExpIMAtmAal5VclLogicalIndexEntry,_H:oacExpIMAtmAal5VclLogicalIndexIfIndex,'oacExpIMAtmAal5Notifications':oacExpIMAtmAal5Notifications})