_E='read-only'
_D='swLedInfoUnitId'
_C='DGS3120-24PC-LED-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dlink_Dgs3120Proj_DGS_3120_24PC_bx,=mibBuilder.importSymbols('SWDGS3120PRIMGMT-MIB','dlink-Dgs3120Proj-DGS-3120-24PC-bx')
swLedMIB=ModuleIdentity((1,3,6,1,4,1,171,11,117,3,1,4))
_SwLedMIBObject_ObjectIdentity=ObjectIdentity
swLedMIBObject=_SwLedMIBObject_ObjectIdentity((1,3,6,1,4,1,171,11,117,3,1,4,1))
_SwLedInfoTable_Object=MibTable
swLedInfoTable=_SwLedInfoTable_Object((1,3,6,1,4,1,171,11,117,3,1,4,1,1))
if mibBuilder.loadTexts:swLedInfoTable.setStatus(_A)
_SwLedInfoEntry_Object=MibTableRow
swLedInfoEntry=_SwLedInfoEntry_Object((1,3,6,1,4,1,171,11,117,3,1,4,1,1,1))
swLedInfoEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:swLedInfoEntry.setStatus(_A)
class _SwLedInfoUnitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,13))
_SwLedInfoUnitId_Type.__name__=_B
_SwLedInfoUnitId_Object=MibTableColumn
swLedInfoUnitId=_SwLedInfoUnitId_Object((1,3,6,1,4,1,171,11,117,3,1,4,1,1,1,1),_SwLedInfoUnitId_Type())
swLedInfoUnitId.setMaxAccess(_E)
if mibBuilder.loadTexts:swLedInfoUnitId.setStatus(_A)
_SwLedInfoFrontPanelLedStatus_Type=OctetString
_SwLedInfoFrontPanelLedStatus_Object=MibTableColumn
swLedInfoFrontPanelLedStatus=_SwLedInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,117,3,1,4,1,1,1,2),_SwLedInfoFrontPanelLedStatus_Type())
swLedInfoFrontPanelLedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swLedInfoFrontPanelLedStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'swLedMIB':swLedMIB,'swLedMIBObject':swLedMIBObject,'swLedInfoTable':swLedInfoTable,'swLedInfoEntry':swLedInfoEntry,_D:swLedInfoUnitId,'swLedInfoFrontPanelLedStatus':swLedInfoFrontPanelLedStatus})