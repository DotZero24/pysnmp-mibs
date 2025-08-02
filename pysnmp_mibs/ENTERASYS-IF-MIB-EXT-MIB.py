_H='etsysIfMibExtOperStatusGroup'
_G='etsysIfMibExtOperLinkGroup'
_F='etsysIfOperStatusCause'
_E='etsysIfOperStateLinkChange'
_D='etsysInterfaceExtEntry'
_C='EnabledStatus'
_B='ENTERASYS-IF-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifEntry,=mibBuilder.importSymbols('IF-MIB','ifEntry')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysIfMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,57))
if mibBuilder.loadTexts:etsysIfMibExtMIB.setRevisions(('2015-04-14 12:39','2014-07-24 13:22','2013-04-12 13:14','2013-02-11 18:14','2012-02-02 20:08','2011-12-07 15:58','2011-10-25 19:48','2011-06-08 12:12','2011-05-12 14:15','2005-01-13 21:35'))
class EtsysIfOperStatusCauses(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('adminStatus',0),('linkLoss',1),('linkFlap',2),('self',3),('initialization',4),('flowLimiting',5),('policy',6),('classOfService',7),('ieee8021x',8),('ieee8023lag',9),('enetOam',10),('enetOamLb',11),('macLock',12),('chassisBonding',13),('linkState',14),('enetOamUld',15),('txqMonitor',16),('priorityFlowControl',17),('macSec',18)))
_EtsysIfMibExtObjects_ObjectIdentity=ObjectIdentity
etsysIfMibExtObjects=_EtsysIfMibExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,57,1))
_EtsysIfMibExtSystem_ObjectIdentity=ObjectIdentity
etsysIfMibExtSystem=_EtsysIfMibExtSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,57,1,1))
class _EtsysIfOperStateLinkChange_Type(EnabledStatus):defaultValue=2
_EtsysIfOperStateLinkChange_Type.__name__=_C
_EtsysIfOperStateLinkChange_Object=MibScalar
etsysIfOperStateLinkChange=_EtsysIfOperStateLinkChange_Object((1,3,6,1,4,1,5624,1,2,57,1,1,1),_EtsysIfOperStateLinkChange_Type())
etsysIfOperStateLinkChange.setMaxAccess('read-write')
if mibBuilder.loadTexts:etsysIfOperStateLinkChange.setStatus(_A)
_EtsysIfMibExtInterface_ObjectIdentity=ObjectIdentity
etsysIfMibExtInterface=_EtsysIfMibExtInterface_ObjectIdentity((1,3,6,1,4,1,5624,1,2,57,1,2))
_EtsysInterfaceExtTable_Object=MibTable
etsysInterfaceExtTable=_EtsysInterfaceExtTable_Object((1,3,6,1,4,1,5624,1,2,57,1,2,1))
if mibBuilder.loadTexts:etsysInterfaceExtTable.setStatus(_A)
_EtsysInterfaceExtEntry_Object=MibTableRow
etsysInterfaceExtEntry=_EtsysInterfaceExtEntry_Object((1,3,6,1,4,1,5624,1,2,57,1,2,1,1))
if mibBuilder.loadTexts:etsysInterfaceExtEntry.setStatus(_A)
_EtsysIfOperStatusCause_Type=EtsysIfOperStatusCauses
_EtsysIfOperStatusCause_Object=MibTableColumn
etsysIfOperStatusCause=_EtsysIfOperStatusCause_Object((1,3,6,1,4,1,5624,1,2,57,1,2,1,1,1),_EtsysIfOperStatusCause_Type())
etsysIfOperStatusCause.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysIfOperStatusCause.setStatus(_A)
_EtsysIfMibExtConformance_ObjectIdentity=ObjectIdentity
etsysIfMibExtConformance=_EtsysIfMibExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,57,2))
_EtsysIfMibExtGroups_ObjectIdentity=ObjectIdentity
etsysIfMibExtGroups=_EtsysIfMibExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,57,2,1))
_EtsysIfMibExtCompliances_ObjectIdentity=ObjectIdentity
etsysIfMibExtCompliances=_EtsysIfMibExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,57,2,2))
ifEntry.registerAugmentions((_B,_D))
etsysInterfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())
etsysIfMibExtOperLinkGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,57,2,1,1))
etsysIfMibExtOperLinkGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:etsysIfMibExtOperLinkGroup.setStatus(_A)
etsysIfMibExtOperStatusGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,57,2,1,2))
etsysIfMibExtOperStatusGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:etsysIfMibExtOperStatusGroup.setStatus(_A)
etsysIfMibExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,57,2,2,1))
etsysIfMibExtCompliance.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:etsysIfMibExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EtsysIfOperStatusCauses':EtsysIfOperStatusCauses,'etsysIfMibExtMIB':etsysIfMibExtMIB,'etsysIfMibExtObjects':etsysIfMibExtObjects,'etsysIfMibExtSystem':etsysIfMibExtSystem,_E:etsysIfOperStateLinkChange,'etsysIfMibExtInterface':etsysIfMibExtInterface,'etsysInterfaceExtTable':etsysInterfaceExtTable,_D:etsysInterfaceExtEntry,_F:etsysIfOperStatusCause,'etsysIfMibExtConformance':etsysIfMibExtConformance,'etsysIfMibExtGroups':etsysIfMibExtGroups,_G:etsysIfMibExtOperLinkGroup,_H:etsysIfMibExtOperStatusGroup,'etsysIfMibExtCompliances':etsysIfMibExtCompliances,'etsysIfMibExtCompliance':etsysIfMibExtCompliance})