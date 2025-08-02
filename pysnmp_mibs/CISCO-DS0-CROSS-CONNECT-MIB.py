_K='cDs0CrossConnectConfigGroup'
_J='cds0ConnRowStatus'
_I='cds0Endpt2Ds0Group'
_H='cds0Endpt2Ds1'
_G='not-accessible'
_F='cds0Endpt1Ds0Group'
_E='cds0Endpt1Ds1'
_D='read-create'
_C='Unsigned32'
_B='CISCO-DS0-CROSS-CONNECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoDs0CrossConnectMIB=ModuleIdentity((1,3,6,1,4,1,9,9,9999))
if mibBuilder.loadTexts:ciscoDs0CrossConnectMIB.setRevisions(('2003-03-05 00:00',))
_CiscoDs0CrossConnectMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDs0CrossConnectMIBNotifs=_CiscoDs0CrossConnectMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,9999,0))
_CiscoDs0CrossConnectMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDs0CrossConnectMIBObjects=_CiscoDs0CrossConnectMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1))
_CDs0CrossConnectConfig_ObjectIdentity=ObjectIdentity
cDs0CrossConnectConfig=_CDs0CrossConnectConfig_ObjectIdentity((1,3,6,1,4,1,9,9,9999,1,1))
_Cds0CrossConnectConfigTable_Object=MibTable
cds0CrossConnectConfigTable=_Cds0CrossConnectConfigTable_Object((1,3,6,1,4,1,9,9,9999,1,1,1))
if mibBuilder.loadTexts:cds0CrossConnectConfigTable.setStatus(_A)
_Cds0CrossConnectConfigEntry_Object=MibTableRow
cds0CrossConnectConfigEntry=_Cds0CrossConnectConfigEntry_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1))
cds0CrossConnectConfigEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:cds0CrossConnectConfigEntry.setStatus(_A)
_Cds0Endpt1Ds1_Type=InterfaceIndex
_Cds0Endpt1Ds1_Object=MibTableColumn
cds0Endpt1Ds1=_Cds0Endpt1Ds1_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,1),_Cds0Endpt1Ds1_Type())
cds0Endpt1Ds1.setMaxAccess(_G)
if mibBuilder.loadTexts:cds0Endpt1Ds1.setStatus(_A)
class _Cds0Endpt1Ds0Group_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Cds0Endpt1Ds0Group_Type.__name__=_C
_Cds0Endpt1Ds0Group_Object=MibTableColumn
cds0Endpt1Ds0Group=_Cds0Endpt1Ds0Group_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,2),_Cds0Endpt1Ds0Group_Type())
cds0Endpt1Ds0Group.setMaxAccess(_G)
if mibBuilder.loadTexts:cds0Endpt1Ds0Group.setStatus(_A)
_Cds0Endpt2Ds1_Type=InterfaceIndex
_Cds0Endpt2Ds1_Object=MibTableColumn
cds0Endpt2Ds1=_Cds0Endpt2Ds1_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,3),_Cds0Endpt2Ds1_Type())
cds0Endpt2Ds1.setMaxAccess(_D)
if mibBuilder.loadTexts:cds0Endpt2Ds1.setStatus(_A)
class _Cds0Endpt2Ds0Group_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Cds0Endpt2Ds0Group_Type.__name__=_C
_Cds0Endpt2Ds0Group_Object=MibTableColumn
cds0Endpt2Ds0Group=_Cds0Endpt2Ds0Group_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,4),_Cds0Endpt2Ds0Group_Type())
cds0Endpt2Ds0Group.setMaxAccess(_D)
if mibBuilder.loadTexts:cds0Endpt2Ds0Group.setStatus(_A)
_Cds0ConnRowStatus_Type=RowStatus
_Cds0ConnRowStatus_Object=MibTableColumn
cds0ConnRowStatus=_Cds0ConnRowStatus_Object((1,3,6,1,4,1,9,9,9999,1,1,1,1,5),_Cds0ConnRowStatus_Type())
cds0ConnRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cds0ConnRowStatus.setStatus(_A)
_CiscoDs0CrossConnectMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDs0CrossConnectMIBConformance=_CiscoDs0CrossConnectMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2))
_CiscoDs0CrossConnectMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDs0CrossConnectMIBCompliances=_CiscoDs0CrossConnectMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,1))
_CiscoDs0CrossConnectMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDs0CrossConnectMIBGroups=_CiscoDs0CrossConnectMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,9999,2,2))
cDs0CrossConnectConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,9999,2,2,1))
cDs0CrossConnectConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cDs0CrossConnectConfigGroup.setStatus(_A)
ciscoDs0CrossConnectMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,9999,2,1,1))
ciscoDs0CrossConnectMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoDs0CrossConnectMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDs0CrossConnectMIB':ciscoDs0CrossConnectMIB,'ciscoDs0CrossConnectMIBNotifs':ciscoDs0CrossConnectMIBNotifs,'ciscoDs0CrossConnectMIBObjects':ciscoDs0CrossConnectMIBObjects,'cDs0CrossConnectConfig':cDs0CrossConnectConfig,'cds0CrossConnectConfigTable':cds0CrossConnectConfigTable,'cds0CrossConnectConfigEntry':cds0CrossConnectConfigEntry,_E:cds0Endpt1Ds1,_F:cds0Endpt1Ds0Group,_H:cds0Endpt2Ds1,_I:cds0Endpt2Ds0Group,_J:cds0ConnRowStatus,'ciscoDs0CrossConnectMIBConformance':ciscoDs0CrossConnectMIBConformance,'ciscoDs0CrossConnectMIBCompliances':ciscoDs0CrossConnectMIBCompliances,'ciscoDs0CrossConnectMIBCompliance':ciscoDs0CrossConnectMIBCompliance,'ciscoDs0CrossConnectMIBGroups':ciscoDs0CrossConnectMIBGroups,_K:cDs0CrossConnectConfigGroup})