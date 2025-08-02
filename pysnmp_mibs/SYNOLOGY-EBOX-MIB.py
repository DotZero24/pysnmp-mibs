_H='synologyEboxGroup'
_G='eboxRedundantPower'
_F='eboxPower'
_E='eboxModel'
_D='eboxIndex'
_C='read-only'
_B='SYNOLOGY-EBOX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synologyEbox=ModuleIdentity((1,3,6,1,4,1,6574,105))
if mibBuilder.loadTexts:synologyEbox.setRevisions(('2017-06-26 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_EboxTable_Object=MibTable
eboxTable=_EboxTable_Object((1,3,6,1,4,1,6574,105,1))
if mibBuilder.loadTexts:eboxTable.setStatus(_A)
_EboxEntry_Object=MibTableRow
eboxEntry=_EboxEntry_Object((1,3,6,1,4,1,6574,105,1,1))
eboxEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:eboxEntry.setStatus(_A)
_EboxIndex_Type=Integer32
_EboxIndex_Object=MibTableColumn
eboxIndex=_EboxIndex_Object((1,3,6,1,4,1,6574,105,1,1,1),_EboxIndex_Type())
eboxIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eboxIndex.setStatus(_A)
_EboxModel_Type=OctetString
_EboxModel_Object=MibTableColumn
eboxModel=_EboxModel_Object((1,3,6,1,4,1,6574,105,1,1,2),_EboxModel_Type())
eboxModel.setMaxAccess(_C)
if mibBuilder.loadTexts:eboxModel.setStatus(_A)
_EboxPower_Type=Integer32
_EboxPower_Object=MibTableColumn
eboxPower=_EboxPower_Object((1,3,6,1,4,1,6574,105,1,1,3),_EboxPower_Type())
eboxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:eboxPower.setStatus(_A)
_EboxRedundantPower_Type=Integer32
_EboxRedundantPower_Object=MibTableColumn
eboxRedundantPower=_EboxRedundantPower_Object((1,3,6,1,4,1,6574,105,1,1,4),_EboxRedundantPower_Type())
eboxRedundantPower.setMaxAccess(_C)
if mibBuilder.loadTexts:eboxRedundantPower.setStatus(_A)
_SynologyEboxConformance_ObjectIdentity=ObjectIdentity
synologyEboxConformance=_SynologyEboxConformance_ObjectIdentity((1,3,6,1,4,1,6574,105,2))
_SynologyEboxCompliances_ObjectIdentity=ObjectIdentity
synologyEboxCompliances=_SynologyEboxCompliances_ObjectIdentity((1,3,6,1,4,1,6574,105,2,1))
_SynologyEboxGroups_ObjectIdentity=ObjectIdentity
synologyEboxGroups=_SynologyEboxGroups_ObjectIdentity((1,3,6,1,4,1,6574,105,2,2))
synologyEboxGroup=ObjectGroup((1,3,6,1,4,1,6574,105,2,2,1))
synologyEboxGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:synologyEboxGroup.setStatus(_A)
synologyEboxCompliance=ModuleCompliance((1,3,6,1,4,1,6574,105,2,1,1))
synologyEboxCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:synologyEboxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synologyEbox':synologyEbox,'eboxTable':eboxTable,'eboxEntry':eboxEntry,_D:eboxIndex,_E:eboxModel,_F:eboxPower,_G:eboxRedundantPower,'synologyEboxConformance':synologyEboxConformance,'synologyEboxCompliances':synologyEboxCompliances,'synologyEboxCompliance':synologyEboxCompliance,'synologyEboxGroups':synologyEboxGroups,_H:synologyEboxGroup})