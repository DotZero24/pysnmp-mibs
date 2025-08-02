_L='ifCapStackGroup'
_K='ifInvCapStackStatus'
_J='ifCapStackStatus'
_I='read-only'
_H='ifStackGroup2'
_G='ifInvStackGroup'
_F='IF-INVERTED-STACK-MIB'
_E='ifStackLowerLayer'
_D='ifStackHigherLayer'
_C='IF-CAP-STACK-MIB'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifInvStackGroup,=mibBuilder.importSymbols(_F,_G)
ifStackGroup2,ifStackHigherLayer,ifStackLowerLayer=mibBuilder.importSymbols(_B,_H,_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ifCapStackMIB=ModuleIdentity((1,3,6,1,2,1,166))
if mibBuilder.loadTexts:ifCapStackMIB.setRevisions(('2007-11-07 00:00',))
_IfCapStackObjects_ObjectIdentity=ObjectIdentity
ifCapStackObjects=_IfCapStackObjects_ObjectIdentity((1,3,6,1,2,1,166,1))
_IfCapStackTable_Object=MibTable
ifCapStackTable=_IfCapStackTable_Object((1,3,6,1,2,1,166,1,1))
if mibBuilder.loadTexts:ifCapStackTable.setStatus(_A)
_IfCapStackEntry_Object=MibTableRow
ifCapStackEntry=_IfCapStackEntry_Object((1,3,6,1,2,1,166,1,1,1))
ifCapStackEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:ifCapStackEntry.setStatus(_A)
_IfCapStackStatus_Type=TruthValue
_IfCapStackStatus_Object=MibTableColumn
ifCapStackStatus=_IfCapStackStatus_Object((1,3,6,1,2,1,166,1,1,1,1),_IfCapStackStatus_Type())
ifCapStackStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ifCapStackStatus.setStatus(_A)
_IfInvCapStackTable_Object=MibTable
ifInvCapStackTable=_IfInvCapStackTable_Object((1,3,6,1,2,1,166,1,2))
if mibBuilder.loadTexts:ifInvCapStackTable.setStatus(_A)
_IfInvCapStackEntry_Object=MibTableRow
ifInvCapStackEntry=_IfInvCapStackEntry_Object((1,3,6,1,2,1,166,1,2,1))
ifInvCapStackEntry.setIndexNames((0,_B,_E),(0,_B,_D))
if mibBuilder.loadTexts:ifInvCapStackEntry.setStatus(_A)
_IfInvCapStackStatus_Type=TruthValue
_IfInvCapStackStatus_Object=MibTableColumn
ifInvCapStackStatus=_IfInvCapStackStatus_Object((1,3,6,1,2,1,166,1,2,1,1),_IfInvCapStackStatus_Type())
ifInvCapStackStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ifInvCapStackStatus.setStatus(_A)
_IfCapStackConformance_ObjectIdentity=ObjectIdentity
ifCapStackConformance=_IfCapStackConformance_ObjectIdentity((1,3,6,1,2,1,166,2))
_IfCapStackGroups_ObjectIdentity=ObjectIdentity
ifCapStackGroups=_IfCapStackGroups_ObjectIdentity((1,3,6,1,2,1,166,2,1))
_IfCapStackCompliances_ObjectIdentity=ObjectIdentity
ifCapStackCompliances=_IfCapStackCompliances_ObjectIdentity((1,3,6,1,2,1,166,2,2))
ifCapStackGroup=ObjectGroup((1,3,6,1,2,1,166,2,1,1))
ifCapStackGroup.setObjects(*((_C,_J),(_C,_K)))
if mibBuilder.loadTexts:ifCapStackGroup.setStatus(_A)
ifCapStackCompliance=ModuleCompliance((1,3,6,1,2,1,166,2,2,1))
ifCapStackCompliance.setObjects(*((_C,_L),(_B,_H),(_F,_G)))
if mibBuilder.loadTexts:ifCapStackCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ifCapStackMIB':ifCapStackMIB,'ifCapStackObjects':ifCapStackObjects,'ifCapStackTable':ifCapStackTable,'ifCapStackEntry':ifCapStackEntry,_J:ifCapStackStatus,'ifInvCapStackTable':ifInvCapStackTable,'ifInvCapStackEntry':ifInvCapStackEntry,_K:ifInvCapStackStatus,'ifCapStackConformance':ifCapStackConformance,'ifCapStackGroups':ifCapStackGroups,_L:ifCapStackGroup,'ifCapStackCompliances':ifCapStackCompliances,'ifCapStackCompliance':ifCapStackCompliance})