_K='mitelGrpAppCmn'
_J='mitelAppTblAppAlrmStatus'
_I='mitelAppTblProductDescr'
_H='mitelAppTblProductVersion'
_G='mitelAppTblProductName'
_F='mitelAppTblProductManufacturer'
_E='Integer32'
_D='mitelAppTblProductOid'
_C='read-only'
_B='MITEL-APPCMN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ItuPerceivedSeverity,=mibBuilder.importSymbols('MITEL-CMNALM-MIB','ItuPerceivedSeverity')
mitelConfCompliances,mitelConfGroups,mitelIdentification,mitelPropApplications=mibBuilder.importSymbols('MITEL-MIB','mitelConfCompliances','mitelConfGroups','mitelIdentification','mitelPropApplications')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelAppCommon=ModuleIdentity((1,3,6,1,4,1,1027,4,1,2))
if mibBuilder.loadTexts:mitelAppCommon.setRevisions(('2014-02-11 12:00','2005-02-21 21:34','2004-01-30 00:00'))
_MitelAppCmnObjects_ObjectIdentity=ObjectIdentity
mitelAppCmnObjects=_MitelAppCmnObjects_ObjectIdentity((1,3,6,1,4,1,1027,4,1,2,1))
if mibBuilder.loadTexts:mitelAppCmnObjects.setStatus(_A)
_MitelAppTable_Object=MibTable
mitelAppTable=_MitelAppTable_Object((1,3,6,1,4,1,1027,4,1,2,1,1))
if mibBuilder.loadTexts:mitelAppTable.setStatus(_A)
_MitelAppTableEntry_Object=MibTableRow
mitelAppTableEntry=_MitelAppTableEntry_Object((1,3,6,1,4,1,1027,4,1,2,1,1,1))
mitelAppTableEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:mitelAppTableEntry.setStatus(_A)
_MitelAppTblProductOid_Type=ObjectIdentifier
_MitelAppTblProductOid_Object=MibTableColumn
mitelAppTblProductOid=_MitelAppTblProductOid_Object((1,3,6,1,4,1,1027,4,1,2,1,1,1,1),_MitelAppTblProductOid_Type())
mitelAppTblProductOid.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelAppTblProductOid.setStatus(_A)
_MitelAppTblProductManufacturer_Type=DisplayString
_MitelAppTblProductManufacturer_Object=MibTableColumn
mitelAppTblProductManufacturer=_MitelAppTblProductManufacturer_Object((1,3,6,1,4,1,1027,4,1,2,1,1,1,2),_MitelAppTblProductManufacturer_Type())
mitelAppTblProductManufacturer.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelAppTblProductManufacturer.setStatus(_A)
_MitelAppTblProductName_Type=DisplayString
_MitelAppTblProductName_Object=MibTableColumn
mitelAppTblProductName=_MitelAppTblProductName_Object((1,3,6,1,4,1,1027,4,1,2,1,1,1,3),_MitelAppTblProductName_Type())
mitelAppTblProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelAppTblProductName.setStatus(_A)
_MitelAppTblProductVersion_Type=DisplayString
_MitelAppTblProductVersion_Object=MibTableColumn
mitelAppTblProductVersion=_MitelAppTblProductVersion_Object((1,3,6,1,4,1,1027,4,1,2,1,1,1,4),_MitelAppTblProductVersion_Type())
mitelAppTblProductVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelAppTblProductVersion.setStatus(_A)
_MitelAppTblProductDescr_Type=DisplayString
_MitelAppTblProductDescr_Object=MibTableColumn
mitelAppTblProductDescr=_MitelAppTblProductDescr_Object((1,3,6,1,4,1,1027,4,1,2,1,1,1,5),_MitelAppTblProductDescr_Type())
mitelAppTblProductDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelAppTblProductDescr.setStatus(_A)
_MitelAppTblAppAlrmStatus_Type=ItuPerceivedSeverity
_MitelAppTblAppAlrmStatus_Object=MibTableColumn
mitelAppTblAppAlrmStatus=_MitelAppTblAppAlrmStatus_Object((1,3,6,1,4,1,1027,4,1,2,1,1,1,6),_MitelAppTblAppAlrmStatus_Type())
mitelAppTblAppAlrmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelAppTblAppAlrmStatus.setStatus(_A)
class _MitelAppNumberOfApps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MitelAppNumberOfApps_Type.__name__=_E
_MitelAppNumberOfApps_Object=MibScalar
mitelAppNumberOfApps=_MitelAppNumberOfApps_Object((1,3,6,1,4,1,1027,4,1,2,1,2),_MitelAppNumberOfApps_Type())
mitelAppNumberOfApps.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelAppNumberOfApps.setStatus(_A)
_MitelComplAppCommon_ObjectIdentity=ObjectIdentity
mitelComplAppCommon=_MitelComplAppCommon_ObjectIdentity((1,3,6,1,4,1,1027,5,1,5))
if mibBuilder.loadTexts:mitelComplAppCommon.setStatus(_A)
_MitelGrpAppCommon_ObjectIdentity=ObjectIdentity
mitelGrpAppCommon=_MitelGrpAppCommon_ObjectIdentity((1,3,6,1,4,1,1027,5,2,3))
if mibBuilder.loadTexts:mitelGrpAppCommon.setStatus(_A)
mitelGrpAppCmn=ObjectGroup((1,3,6,1,4,1,1027,5,2,3,1))
mitelGrpAppCmn.setObjects(*((_B,_D),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:mitelGrpAppCmn.setStatus(_A)
mitelComplAppCmn=ModuleCompliance((1,3,6,1,4,1,1027,5,1,5,1))
mitelComplAppCmn.setObjects((_B,_K))
if mibBuilder.loadTexts:mitelComplAppCmn.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mitelAppCommon':mitelAppCommon,'mitelAppCmnObjects':mitelAppCmnObjects,'mitelAppTable':mitelAppTable,'mitelAppTableEntry':mitelAppTableEntry,_D:mitelAppTblProductOid,_F:mitelAppTblProductManufacturer,_G:mitelAppTblProductName,_H:mitelAppTblProductVersion,_I:mitelAppTblProductDescr,_J:mitelAppTblAppAlrmStatus,'mitelAppNumberOfApps':mitelAppNumberOfApps,'mitelComplAppCommon':mitelComplAppCommon,'mitelComplAppCmn':mitelComplAppCmn,'mitelGrpAppCommon':mitelGrpAppCommon,_K:mitelGrpAppCmn})