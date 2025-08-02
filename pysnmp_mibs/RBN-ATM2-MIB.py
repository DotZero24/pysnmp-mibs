_K='rbnAtm2HostGroup'
_J='rbnAtm2CommonStatsGroup'
_I='rbnAtm2Aal5VclOutPktDrops'
_H='rbnAtm2VclOutPktDrops'
_G='rbnAtm2VplOutPktDrops'
_F='rbnAtm2Aal5VclStatEntry'
_E='rbnAtm2VclStatEntry'
_D='rbnAtm2VplStatEntry'
_C='read-only'
_B='RBN-ATM2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmAal5VclStatEntry,atmVclStatEntry,atmVplStatEntry=mibBuilder.importSymbols('ATM2-MIB','atmAal5VclStatEntry','atmVclStatEntry','atmVplStatEntry')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnAtm2MIB=ModuleIdentity((1,3,6,1,4,1,2352,2,50))
if mibBuilder.loadTexts:rbnAtm2MIB.setRevisions(('2009-06-11 17:00',))
_RbnAtm2MIBObjects_ObjectIdentity=ObjectIdentity
rbnAtm2MIBObjects=_RbnAtm2MIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,50,1))
_RbnAtm2VplStatTable_Object=MibTable
rbnAtm2VplStatTable=_RbnAtm2VplStatTable_Object((1,3,6,1,4,1,2352,2,50,1,1))
if mibBuilder.loadTexts:rbnAtm2VplStatTable.setStatus(_A)
_RbnAtm2VplStatEntry_Object=MibTableRow
rbnAtm2VplStatEntry=_RbnAtm2VplStatEntry_Object((1,3,6,1,4,1,2352,2,50,1,1,1))
if mibBuilder.loadTexts:rbnAtm2VplStatEntry.setStatus(_A)
_RbnAtm2VplOutPktDrops_Type=Counter32
_RbnAtm2VplOutPktDrops_Object=MibTableColumn
rbnAtm2VplOutPktDrops=_RbnAtm2VplOutPktDrops_Object((1,3,6,1,4,1,2352,2,50,1,1,1,1),_RbnAtm2VplOutPktDrops_Type())
rbnAtm2VplOutPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtm2VplOutPktDrops.setStatus(_A)
_RbnAtm2VclStatTable_Object=MibTable
rbnAtm2VclStatTable=_RbnAtm2VclStatTable_Object((1,3,6,1,4,1,2352,2,50,1,2))
if mibBuilder.loadTexts:rbnAtm2VclStatTable.setStatus(_A)
_RbnAtm2VclStatEntry_Object=MibTableRow
rbnAtm2VclStatEntry=_RbnAtm2VclStatEntry_Object((1,3,6,1,4,1,2352,2,50,1,2,1))
if mibBuilder.loadTexts:rbnAtm2VclStatEntry.setStatus(_A)
_RbnAtm2VclOutPktDrops_Type=Counter32
_RbnAtm2VclOutPktDrops_Object=MibTableColumn
rbnAtm2VclOutPktDrops=_RbnAtm2VclOutPktDrops_Object((1,3,6,1,4,1,2352,2,50,1,2,1,1),_RbnAtm2VclOutPktDrops_Type())
rbnAtm2VclOutPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtm2VclOutPktDrops.setStatus(_A)
_RbnAtm2Aal5VclStatTable_Object=MibTable
rbnAtm2Aal5VclStatTable=_RbnAtm2Aal5VclStatTable_Object((1,3,6,1,4,1,2352,2,50,1,3))
if mibBuilder.loadTexts:rbnAtm2Aal5VclStatTable.setStatus(_A)
_RbnAtm2Aal5VclStatEntry_Object=MibTableRow
rbnAtm2Aal5VclStatEntry=_RbnAtm2Aal5VclStatEntry_Object((1,3,6,1,4,1,2352,2,50,1,3,1))
if mibBuilder.loadTexts:rbnAtm2Aal5VclStatEntry.setStatus(_A)
_RbnAtm2Aal5VclOutPktDrops_Type=Counter32
_RbnAtm2Aal5VclOutPktDrops_Object=MibTableColumn
rbnAtm2Aal5VclOutPktDrops=_RbnAtm2Aal5VclOutPktDrops_Object((1,3,6,1,4,1,2352,2,50,1,3,1,1),_RbnAtm2Aal5VclOutPktDrops_Type())
rbnAtm2Aal5VclOutPktDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtm2Aal5VclOutPktDrops.setStatus(_A)
_RbnAtm2MIBConformance_ObjectIdentity=ObjectIdentity
rbnAtm2MIBConformance=_RbnAtm2MIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,50,2))
_RbnAtm2MIBCompliances_ObjectIdentity=ObjectIdentity
rbnAtm2MIBCompliances=_RbnAtm2MIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,50,2,1))
_RbnAtm2MIBGroups_ObjectIdentity=ObjectIdentity
rbnAtm2MIBGroups=_RbnAtm2MIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,50,2,2))
atmVplStatEntry.registerAugmentions((_B,_D))
rbnAtm2VplStatEntry.setIndexNames(*atmVplStatEntry.getIndexNames())
atmVclStatEntry.registerAugmentions((_B,_E))
rbnAtm2VclStatEntry.setIndexNames(*atmVclStatEntry.getIndexNames())
atmAal5VclStatEntry.registerAugmentions((_B,_F))
rbnAtm2Aal5VclStatEntry.setIndexNames(*atmAal5VclStatEntry.getIndexNames())
rbnAtm2CommonStatsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,50,2,2,1))
rbnAtm2CommonStatsGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:rbnAtm2CommonStatsGroup.setStatus(_A)
rbnAtm2HostGroup=ObjectGroup((1,3,6,1,4,1,2352,2,50,2,2,2))
rbnAtm2HostGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:rbnAtm2HostGroup.setStatus(_A)
rbnAtm2Compliance=ModuleCompliance((1,3,6,1,4,1,2352,2,50,2,1,1))
rbnAtm2Compliance.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:rbnAtm2Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnAtm2MIB':rbnAtm2MIB,'rbnAtm2MIBObjects':rbnAtm2MIBObjects,'rbnAtm2VplStatTable':rbnAtm2VplStatTable,_D:rbnAtm2VplStatEntry,_G:rbnAtm2VplOutPktDrops,'rbnAtm2VclStatTable':rbnAtm2VclStatTable,_E:rbnAtm2VclStatEntry,_H:rbnAtm2VclOutPktDrops,'rbnAtm2Aal5VclStatTable':rbnAtm2Aal5VclStatTable,_F:rbnAtm2Aal5VclStatEntry,_I:rbnAtm2Aal5VclOutPktDrops,'rbnAtm2MIBConformance':rbnAtm2MIBConformance,'rbnAtm2MIBCompliances':rbnAtm2MIBCompliances,'rbnAtm2Compliance':rbnAtm2Compliance,'rbnAtm2MIBGroups':rbnAtm2MIBGroups,_J:rbnAtm2CommonStatsGroup,_K:rbnAtm2HostGroup})