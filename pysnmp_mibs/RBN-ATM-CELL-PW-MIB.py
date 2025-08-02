_G='rbnAtmCellPWStatGroup'
_F='rbnAtmCellPWCellConcatDrops'
_E='rbnAtmCellPWOutOfSeqDrops'
_D='read-only'
_C='rbnAtmCellPWCircuitHandle'
_B='RBN-ATM-CELL-PW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnCircuitHandle,=mibBuilder.importSymbols('RBN-TC','RbnCircuitHandle')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnAtmCellPWMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,41))
if mibBuilder.loadTexts:rbnAtmCellPWMIB.setRevisions(('2007-05-30 00:00',))
_RbnAtmCellPWObjects_ObjectIdentity=ObjectIdentity
rbnAtmCellPWObjects=_RbnAtmCellPWObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,41,1))
_RbnAtmCellPWStatTable_Object=MibTable
rbnAtmCellPWStatTable=_RbnAtmCellPWStatTable_Object((1,3,6,1,4,1,2352,2,41,1,1))
if mibBuilder.loadTexts:rbnAtmCellPWStatTable.setStatus(_A)
_RbnAtmCellPWStatEntry_Object=MibTableRow
rbnAtmCellPWStatEntry=_RbnAtmCellPWStatEntry_Object((1,3,6,1,4,1,2352,2,41,1,1,1))
rbnAtmCellPWStatEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rbnAtmCellPWStatEntry.setStatus(_A)
_RbnAtmCellPWCircuitHandle_Type=RbnCircuitHandle
_RbnAtmCellPWCircuitHandle_Object=MibTableColumn
rbnAtmCellPWCircuitHandle=_RbnAtmCellPWCircuitHandle_Object((1,3,6,1,4,1,2352,2,41,1,1,1,1),_RbnAtmCellPWCircuitHandle_Type())
rbnAtmCellPWCircuitHandle.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnAtmCellPWCircuitHandle.setStatus(_A)
_RbnAtmCellPWOutOfSeqDrops_Type=Counter32
_RbnAtmCellPWOutOfSeqDrops_Object=MibTableColumn
rbnAtmCellPWOutOfSeqDrops=_RbnAtmCellPWOutOfSeqDrops_Object((1,3,6,1,4,1,2352,2,41,1,1,1,2),_RbnAtmCellPWOutOfSeqDrops_Type())
rbnAtmCellPWOutOfSeqDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmCellPWOutOfSeqDrops.setStatus(_A)
_RbnAtmCellPWCellConcatDrops_Type=Counter32
_RbnAtmCellPWCellConcatDrops_Object=MibTableColumn
rbnAtmCellPWCellConcatDrops=_RbnAtmCellPWCellConcatDrops_Object((1,3,6,1,4,1,2352,2,41,1,1,1,3),_RbnAtmCellPWCellConcatDrops_Type())
rbnAtmCellPWCellConcatDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:rbnAtmCellPWCellConcatDrops.setStatus(_A)
_RbnAtmCellPWMIBConformance_ObjectIdentity=ObjectIdentity
rbnAtmCellPWMIBConformance=_RbnAtmCellPWMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,41,2))
_RbnAtmCellPWMIBGroups_ObjectIdentity=ObjectIdentity
rbnAtmCellPWMIBGroups=_RbnAtmCellPWMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,41,2,1))
_RbnAtmCellPWMIBCompliances_ObjectIdentity=ObjectIdentity
rbnAtmCellPWMIBCompliances=_RbnAtmCellPWMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,41,2,2))
rbnAtmCellPWStatGroup=ObjectGroup((1,3,6,1,4,1,2352,2,41,2,1,1))
rbnAtmCellPWStatGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:rbnAtmCellPWStatGroup.setStatus(_A)
rbnAtmCellPWMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,41,2,2,1))
rbnAtmCellPWMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:rbnAtmCellPWMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnAtmCellPWMIB':rbnAtmCellPWMIB,'rbnAtmCellPWObjects':rbnAtmCellPWObjects,'rbnAtmCellPWStatTable':rbnAtmCellPWStatTable,'rbnAtmCellPWStatEntry':rbnAtmCellPWStatEntry,_C:rbnAtmCellPWCircuitHandle,_E:rbnAtmCellPWOutOfSeqDrops,_F:rbnAtmCellPWCellConcatDrops,'rbnAtmCellPWMIBConformance':rbnAtmCellPWMIBConformance,'rbnAtmCellPWMIBGroups':rbnAtmCellPWMIBGroups,_G:rbnAtmCellPWStatGroup,'rbnAtmCellPWMIBCompliances':rbnAtmCellPWMIBCompliances,'rbnAtmCellPWMIBCompliance':rbnAtmCellPWMIBCompliance})