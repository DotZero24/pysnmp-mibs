_M='dpCableDiagBasicGroup'
_L='dpCableDiagInterfaceType'
_K='dpCableDiagLinkStatus'
_J='dpCableDiagResultCableLength'
_I='dpCableDiagResultCableStatus'
_H='dpCableDiagIfAction'
_G='no_result'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='DLINKPRIME-CABLE-DIAG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dlinkPrimeCableDiagMIB=ModuleIdentity((1,3,6,1,4,1,171,15,1))
if mibBuilder.loadTexts:dlinkPrimeCableDiagMIB.setRevisions(('2014-04-26 00:00',))
_DpCableDiagNotifications_ObjectIdentity=ObjectIdentity
dpCableDiagNotifications=_DpCableDiagNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,1,0))
_DpCableDiagObjects_ObjectIdentity=ObjectIdentity
dpCableDiagObjects=_DpCableDiagObjects_ObjectIdentity((1,3,6,1,4,1,171,15,1,1))
_DpCableDiagIfTable_Object=MibTable
dpCableDiagIfTable=_DpCableDiagIfTable_Object((1,3,6,1,4,1,171,15,1,1,1))
if mibBuilder.loadTexts:dpCableDiagIfTable.setStatus(_A)
_DpCableDiagIfEntry_Object=MibTableRow
dpCableDiagIfEntry=_DpCableDiagIfEntry_Object((1,3,6,1,4,1,171,15,1,1,1,1))
dpCableDiagIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dpCableDiagIfEntry.setStatus(_A)
class _DpCableDiagIfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOp',1),('test',2),('clear',3)))
_DpCableDiagIfAction_Type.__name__=_C
_DpCableDiagIfAction_Object=MibTableColumn
dpCableDiagIfAction=_DpCableDiagIfAction_Object((1,3,6,1,4,1,171,15,1,1,1,1,1),_DpCableDiagIfAction_Type())
dpCableDiagIfAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:dpCableDiagIfAction.setStatus(_A)
_DpCableDiagResultTable_Object=MibTable
dpCableDiagResultTable=_DpCableDiagResultTable_Object((1,3,6,1,4,1,171,15,1,1,2))
if mibBuilder.loadTexts:dpCableDiagResultTable.setStatus(_A)
_DpCableDiagResultEntry_Object=MibTableRow
dpCableDiagResultEntry=_DpCableDiagResultEntry_Object((1,3,6,1,4,1,171,15,1,1,2,1))
dpCableDiagResultEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dpCableDiagResultEntry.setStatus(_A)
class _DpCableDiagResultCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_G,0),('ok',1),('no_cable',2),('open',3),('short',4),('openshort',5),('crosstalk',6)))
_DpCableDiagResultCableStatus_Type.__name__=_C
_DpCableDiagResultCableStatus_Object=MibTableColumn
dpCableDiagResultCableStatus=_DpCableDiagResultCableStatus_Object((1,3,6,1,4,1,171,15,1,1,2,1,1),_DpCableDiagResultCableStatus_Type())
dpCableDiagResultCableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dpCableDiagResultCableStatus.setStatus(_A)
_DpCableDiagResultCableLength_Type=Integer32
_DpCableDiagResultCableLength_Object=MibTableColumn
dpCableDiagResultCableLength=_DpCableDiagResultCableLength_Object((1,3,6,1,4,1,171,15,1,1,2,1,2),_DpCableDiagResultCableLength_Type())
dpCableDiagResultCableLength.setMaxAccess(_D)
if mibBuilder.loadTexts:dpCableDiagResultCableLength.setStatus(_A)
if mibBuilder.loadTexts:dpCableDiagResultCableLength.setUnits('meters')
class _DpCableDiagLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('up',1),('down',2)))
_DpCableDiagLinkStatus_Type.__name__=_C
_DpCableDiagLinkStatus_Object=MibTableColumn
dpCableDiagLinkStatus=_DpCableDiagLinkStatus_Object((1,3,6,1,4,1,171,15,1,1,2,1,3),_DpCableDiagLinkStatus_Type())
dpCableDiagLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dpCableDiagLinkStatus.setStatus(_A)
class _DpCableDiagInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('type_1000BASET',1),('type_1000BASEX',2)))
_DpCableDiagInterfaceType_Type.__name__=_C
_DpCableDiagInterfaceType_Object=MibTableColumn
dpCableDiagInterfaceType=_DpCableDiagInterfaceType_Object((1,3,6,1,4,1,171,15,1,1,2,1,4),_DpCableDiagInterfaceType_Type())
dpCableDiagInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:dpCableDiagInterfaceType.setStatus(_A)
_DpCableDiagConformance_ObjectIdentity=ObjectIdentity
dpCableDiagConformance=_DpCableDiagConformance_ObjectIdentity((1,3,6,1,4,1,171,15,1,2))
_DpCableDiagCompliances_ObjectIdentity=ObjectIdentity
dpCableDiagCompliances=_DpCableDiagCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,1,2,1))
_DpCableDiagGroups_ObjectIdentity=ObjectIdentity
dpCableDiagGroups=_DpCableDiagGroups_ObjectIdentity((1,3,6,1,4,1,171,15,1,2,1,2))
dpCableDiagBasicGroup=ObjectGroup((1,3,6,1,4,1,171,15,1,2,1,2,1))
dpCableDiagBasicGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:dpCableDiagBasicGroup.setStatus(_A)
dpCableDiagCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,1,2,1,1))
dpCableDiagCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:dpCableDiagCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeCableDiagMIB':dlinkPrimeCableDiagMIB,'dpCableDiagNotifications':dpCableDiagNotifications,'dpCableDiagObjects':dpCableDiagObjects,'dpCableDiagIfTable':dpCableDiagIfTable,'dpCableDiagIfEntry':dpCableDiagIfEntry,_H:dpCableDiagIfAction,'dpCableDiagResultTable':dpCableDiagResultTable,'dpCableDiagResultEntry':dpCableDiagResultEntry,_I:dpCableDiagResultCableStatus,_J:dpCableDiagResultCableLength,_K:dpCableDiagLinkStatus,_L:dpCableDiagInterfaceType,'dpCableDiagConformance':dpCableDiagConformance,'dpCableDiagCompliances':dpCableDiagCompliances,'dpCableDiagCompliance':dpCableDiagCompliance,'dpCableDiagGroups':dpCableDiagGroups,_M:dpCableDiagBasicGroup})