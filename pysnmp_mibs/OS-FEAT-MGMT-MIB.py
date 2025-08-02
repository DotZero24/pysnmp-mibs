_J='osFeatMgmtMandatoryGroup'
_I='osFeatMgmtKey'
_H='osFeatMgmtParam'
_G='osFeatMgmtStatus'
_F='osFeatMgmtId'
_E='OctetString'
_D='read-write'
_C='Integer32'
_B='OS-FEAT-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
osFeatMgmt=ModuleIdentity((1,3,6,1,4,1,6926,2,21))
if mibBuilder.loadTexts:osFeatMgmt.setRevisions(('2010-10-26 00:00',))
_OsFeatMgmtObjects_ObjectIdentity=ObjectIdentity
osFeatMgmtObjects=_OsFeatMgmtObjects_ObjectIdentity((1,3,6,1,4,1,6926,2,21,1))
_OsFeatMgmtTable_Object=MibTable
osFeatMgmtTable=_OsFeatMgmtTable_Object((1,3,6,1,4,1,6926,2,21,1,3))
if mibBuilder.loadTexts:osFeatMgmtTable.setStatus(_A)
_OsFeatMgmtEntry_Object=MibTableRow
osFeatMgmtEntry=_OsFeatMgmtEntry_Object((1,3,6,1,4,1,6926,2,21,1,3,1))
osFeatMgmtEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:osFeatMgmtEntry.setStatus(_A)
class _OsFeatMgmtId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('os940rTL10Gports',1))
_OsFeatMgmtId_Type.__name__=_C
_OsFeatMgmtId_Object=MibTableColumn
osFeatMgmtId=_OsFeatMgmtId_Object((1,3,6,1,4,1,6926,2,21,1,3,1,1),_OsFeatMgmtId_Type())
osFeatMgmtId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:osFeatMgmtId.setStatus(_A)
class _OsFeatMgmtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('other',0),('deny',1),('permit',2)))
_OsFeatMgmtStatus_Type.__name__=_C
_OsFeatMgmtStatus_Object=MibTableColumn
osFeatMgmtStatus=_OsFeatMgmtStatus_Object((1,3,6,1,4,1,6926,2,21,1,3,1,2),_OsFeatMgmtStatus_Type())
osFeatMgmtStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osFeatMgmtStatus.setStatus(_A)
_OsFeatMgmtParam_Type=Unsigned32
_OsFeatMgmtParam_Object=MibTableColumn
osFeatMgmtParam=_OsFeatMgmtParam_Object((1,3,6,1,4,1,6926,2,21,1,3,1,3),_OsFeatMgmtParam_Type())
osFeatMgmtParam.setMaxAccess(_D)
if mibBuilder.loadTexts:osFeatMgmtParam.setStatus(_A)
class _OsFeatMgmtKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_OsFeatMgmtKey_Type.__name__=_E
_OsFeatMgmtKey_Object=MibTableColumn
osFeatMgmtKey=_OsFeatMgmtKey_Object((1,3,6,1,4,1,6926,2,21,1,3,1,4),_OsFeatMgmtKey_Type())
osFeatMgmtKey.setMaxAccess(_D)
if mibBuilder.loadTexts:osFeatMgmtKey.setStatus(_A)
_OsFeatMgmtConformance_ObjectIdentity=ObjectIdentity
osFeatMgmtConformance=_OsFeatMgmtConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,21,100))
_OsFeatMgmtMIBCompliances_ObjectIdentity=ObjectIdentity
osFeatMgmtMIBCompliances=_OsFeatMgmtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,21,100,1))
_OsFeatMgmtMIBGroups_ObjectIdentity=ObjectIdentity
osFeatMgmtMIBGroups=_OsFeatMgmtMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,21,100,2))
osFeatMgmtMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,21,100,2,1))
osFeatMgmtMandatoryGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:osFeatMgmtMandatoryGroup.setStatus(_A)
osFeatMgmtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,21,100,1,1))
osFeatMgmtMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:osFeatMgmtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osFeatMgmt':osFeatMgmt,'osFeatMgmtObjects':osFeatMgmtObjects,'osFeatMgmtTable':osFeatMgmtTable,'osFeatMgmtEntry':osFeatMgmtEntry,_F:osFeatMgmtId,_G:osFeatMgmtStatus,_H:osFeatMgmtParam,_I:osFeatMgmtKey,'osFeatMgmtConformance':osFeatMgmtConformance,'osFeatMgmtMIBCompliances':osFeatMgmtMIBCompliances,'osFeatMgmtMIBCompliance':osFeatMgmtMIBCompliance,'osFeatMgmtMIBGroups':osFeatMgmtMIBGroups,_J:osFeatMgmtMandatoryGroup})