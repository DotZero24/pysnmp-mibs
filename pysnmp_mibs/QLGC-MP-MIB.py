_D='qlgcMPGroup'
_C='qlgcMPEpromStatus'
_B='QLGC-MP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qlogicMgmt,=mibBuilder.importSymbols('QLOGIC-SMI','qlogicMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qlgcMaintenancePanelModule=ModuleIdentity((1,3,6,1,4,1,3873,3,2))
if mibBuilder.loadTexts:qlgcMaintenancePanelModule.setRevisions(('2009-09-29 00:00','2007-03-31 00:00'))
class MPEpromStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('alarm',2)))
_QlgcMPNotifications_ObjectIdentity=ObjectIdentity
qlgcMPNotifications=_QlgcMPNotifications_ObjectIdentity((1,3,6,1,4,1,3873,3,2,0))
_QlgcMPObjects_ObjectIdentity=ObjectIdentity
qlgcMPObjects=_QlgcMPObjects_ObjectIdentity((1,3,6,1,4,1,3873,3,2,1))
_QlgcMPStatus_ObjectIdentity=ObjectIdentity
qlgcMPStatus=_QlgcMPStatus_ObjectIdentity((1,3,6,1,4,1,3873,3,2,1,1))
_QlgcMPEpromStatus_Type=MPEpromStatus
_QlgcMPEpromStatus_Object=MibScalar
qlgcMPEpromStatus=_QlgcMPEpromStatus_Object((1,3,6,1,4,1,3873,3,2,1,1,1),_QlgcMPEpromStatus_Type())
qlgcMPEpromStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:qlgcMPEpromStatus.setStatus(_A)
_QlgcMPConformance_ObjectIdentity=ObjectIdentity
qlgcMPConformance=_QlgcMPConformance_ObjectIdentity((1,3,6,1,4,1,3873,3,2,2))
_QlgcMPGroups_ObjectIdentity=ObjectIdentity
qlgcMPGroups=_QlgcMPGroups_ObjectIdentity((1,3,6,1,4,1,3873,3,2,2,1))
_QlgcMPCompliances_ObjectIdentity=ObjectIdentity
qlgcMPCompliances=_QlgcMPCompliances_ObjectIdentity((1,3,6,1,4,1,3873,3,2,2,2))
qlgcMPGroup=ObjectGroup((1,3,6,1,4,1,3873,3,2,2,1,1))
qlgcMPGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:qlgcMPGroup.setStatus(_A)
qlgcMPStatusChange=NotificationType((1,3,6,1,4,1,3873,3,2,0,1))
qlgcMPStatusChange.setObjects((_B,_C))
if mibBuilder.loadTexts:qlgcMPStatusChange.setStatus(_A)
qlgcMPComplianceV1=ModuleCompliance((1,3,6,1,4,1,3873,3,2,2,2,1))
qlgcMPComplianceV1.setObjects((_B,_D))
if mibBuilder.loadTexts:qlgcMPComplianceV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MPEpromStatus':MPEpromStatus,'qlgcMaintenancePanelModule':qlgcMaintenancePanelModule,'qlgcMPNotifications':qlgcMPNotifications,'qlgcMPStatusChange':qlgcMPStatusChange,'qlgcMPObjects':qlgcMPObjects,'qlgcMPStatus':qlgcMPStatus,_C:qlgcMPEpromStatus,'qlgcMPConformance':qlgcMPConformance,'qlgcMPGroups':qlgcMPGroups,_D:qlgcMPGroup,'qlgcMPCompliances':qlgcMPCompliances,'qlgcMPComplianceV1':qlgcMPComplianceV1})