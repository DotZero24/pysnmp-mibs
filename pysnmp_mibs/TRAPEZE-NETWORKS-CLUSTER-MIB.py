_I='trpzClusterApAssignmentGroup'
_H='trpzClusterApAssignConnectedToSam'
_G='trpzClusterApAssignConnectedToPam'
_F='trpzClusterApAssignSamIp'
_E='trpzClusterApAssignPamIp'
_D='trpzClusterApAssignApNum'
_C='read-only'
_B='TRAPEZE-NETWORKS-CLUSTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
TrpzApNum,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-AP-TC','TrpzApNum')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzClusterMib=ModuleIdentity((1,3,6,1,4,1,14525,4,21))
if mibBuilder.loadTexts:trpzClusterMib.setRevisions(('2011-02-24 00:01',))
_TrpzClusterMibObjects_ObjectIdentity=ObjectIdentity
trpzClusterMibObjects=_TrpzClusterMibObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,21,1))
_TrpzClusterApAssignmentTable_Object=MibTable
trpzClusterApAssignmentTable=_TrpzClusterApAssignmentTable_Object((1,3,6,1,4,1,14525,4,21,1,1))
if mibBuilder.loadTexts:trpzClusterApAssignmentTable.setStatus(_A)
_TrpzClusterApAssignmentEntry_Object=MibTableRow
trpzClusterApAssignmentEntry=_TrpzClusterApAssignmentEntry_Object((1,3,6,1,4,1,14525,4,21,1,1,1))
trpzClusterApAssignmentEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:trpzClusterApAssignmentEntry.setStatus(_A)
_TrpzClusterApAssignApNum_Type=TrpzApNum
_TrpzClusterApAssignApNum_Object=MibTableColumn
trpzClusterApAssignApNum=_TrpzClusterApAssignApNum_Object((1,3,6,1,4,1,14525,4,21,1,1,1,1),_TrpzClusterApAssignApNum_Type())
trpzClusterApAssignApNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:trpzClusterApAssignApNum.setStatus(_A)
_TrpzClusterApAssignPamIp_Type=IpAddress
_TrpzClusterApAssignPamIp_Object=MibTableColumn
trpzClusterApAssignPamIp=_TrpzClusterApAssignPamIp_Object((1,3,6,1,4,1,14525,4,21,1,1,1,2),_TrpzClusterApAssignPamIp_Type())
trpzClusterApAssignPamIp.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClusterApAssignPamIp.setStatus(_A)
_TrpzClusterApAssignSamIp_Type=IpAddress
_TrpzClusterApAssignSamIp_Object=MibTableColumn
trpzClusterApAssignSamIp=_TrpzClusterApAssignSamIp_Object((1,3,6,1,4,1,14525,4,21,1,1,1,3),_TrpzClusterApAssignSamIp_Type())
trpzClusterApAssignSamIp.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClusterApAssignSamIp.setStatus(_A)
_TrpzClusterApAssignConnectedToPam_Type=TruthValue
_TrpzClusterApAssignConnectedToPam_Object=MibTableColumn
trpzClusterApAssignConnectedToPam=_TrpzClusterApAssignConnectedToPam_Object((1,3,6,1,4,1,14525,4,21,1,1,1,4),_TrpzClusterApAssignConnectedToPam_Type())
trpzClusterApAssignConnectedToPam.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClusterApAssignConnectedToPam.setStatus(_A)
_TrpzClusterApAssignConnectedToSam_Type=TruthValue
_TrpzClusterApAssignConnectedToSam_Object=MibTableColumn
trpzClusterApAssignConnectedToSam=_TrpzClusterApAssignConnectedToSam_Object((1,3,6,1,4,1,14525,4,21,1,1,1,5),_TrpzClusterApAssignConnectedToSam_Type())
trpzClusterApAssignConnectedToSam.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzClusterApAssignConnectedToSam.setStatus(_A)
_TrpzClusterConformance_ObjectIdentity=ObjectIdentity
trpzClusterConformance=_TrpzClusterConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,21,2))
_TrpzClusterCompliances_ObjectIdentity=ObjectIdentity
trpzClusterCompliances=_TrpzClusterCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,21,2,1))
_TrpzClusterGroups_ObjectIdentity=ObjectIdentity
trpzClusterGroups=_TrpzClusterGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,21,2,2))
trpzClusterApAssignmentGroup=ObjectGroup((1,3,6,1,4,1,14525,4,21,2,2,1))
trpzClusterApAssignmentGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:trpzClusterApAssignmentGroup.setStatus(_A)
trpzClusterCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,21,2,1,1))
trpzClusterCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:trpzClusterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'trpzClusterMib':trpzClusterMib,'trpzClusterMibObjects':trpzClusterMibObjects,'trpzClusterApAssignmentTable':trpzClusterApAssignmentTable,'trpzClusterApAssignmentEntry':trpzClusterApAssignmentEntry,_D:trpzClusterApAssignApNum,_E:trpzClusterApAssignPamIp,_F:trpzClusterApAssignSamIp,_G:trpzClusterApAssignConnectedToPam,_H:trpzClusterApAssignConnectedToSam,'trpzClusterConformance':trpzClusterConformance,'trpzClusterCompliances':trpzClusterCompliances,'trpzClusterCompliance':trpzClusterCompliance,'trpzClusterGroups':trpzClusterGroups,_I:trpzClusterApAssignmentGroup})