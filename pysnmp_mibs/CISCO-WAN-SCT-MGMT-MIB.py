_S='cwSctFileMgmtObjectGroup'
_R='cwSctFileRowStatus'
_Q='cwSctFileOperStatus'
_P='cwSctFileDescription'
_O='cwSctFileChecksum'
_N='cwSctFileMinorVersion'
_M='cwSctFileName'
_L='cwSctMajorVersion'
_K='cwSctId'
_J='cwSctType'
_I='cwSctCardType'
_H='read-create'
_G='read-only'
_F='SnmpAdminString'
_E='not-accessible'
_D='Unsigned32'
_C='Integer32'
_B='CISCO-WAN-SCT-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoWanSctMgmtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,236))
if mibBuilder.loadTexts:ciscoWanSctMgmtMIB.setRevisions(('2002-05-21 00:00','2001-11-18 00:00','2001-09-17 00:00'))
_CiscoWanSctMgmtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanSctMgmtMIBObjects=_CiscoWanSctMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,236,1))
_CwSctFileMgmtTable_Object=MibTable
cwSctFileMgmtTable=_CwSctFileMgmtTable_Object((1,3,6,1,4,1,9,9,236,1,1))
if mibBuilder.loadTexts:cwSctFileMgmtTable.setStatus(_A)
_CwSctFileMgmtEntry_Object=MibTableRow
cwSctFileMgmtEntry=_CwSctFileMgmtEntry_Object((1,3,6,1,4,1,9,9,236,1,1,1))
cwSctFileMgmtEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:cwSctFileMgmtEntry.setStatus(_A)
class _CwSctCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('axsm',1),('axsme',2),('pxm1e',3),('hsfr',4),('axsmxg',5)))
_CwSctCardType_Type.__name__=_C
_CwSctCardType_Object=MibTableColumn
cwSctCardType=_CwSctCardType_Object((1,3,6,1,4,1,9,9,236,1,1,1,1),_CwSctCardType_Type())
cwSctCardType.setMaxAccess(_E)
if mibBuilder.loadTexts:cwSctCardType.setStatus(_A)
class _CwSctType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portSct',1),('cardSct',2)))
_CwSctType_Type.__name__=_C
_CwSctType_Object=MibTableColumn
cwSctType=_CwSctType_Object((1,3,6,1,4,1,9,9,236,1,1,1,2),_CwSctType_Type())
cwSctType.setMaxAccess(_E)
if mibBuilder.loadTexts:cwSctType.setStatus(_A)
class _CwSctId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwSctId_Type.__name__=_D
_CwSctId_Object=MibTableColumn
cwSctId=_CwSctId_Object((1,3,6,1,4,1,9,9,236,1,1,1,3),_CwSctId_Type())
cwSctId.setMaxAccess(_E)
if mibBuilder.loadTexts:cwSctId.setStatus(_A)
class _CwSctMajorVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwSctMajorVersion_Type.__name__=_D
_CwSctMajorVersion_Object=MibTableColumn
cwSctMajorVersion=_CwSctMajorVersion_Object((1,3,6,1,4,1,9,9,236,1,1,1,4),_CwSctMajorVersion_Type())
cwSctMajorVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:cwSctMajorVersion.setStatus(_A)
class _CwSctFileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,132))
_CwSctFileName_Type.__name__=_F
_CwSctFileName_Object=MibTableColumn
cwSctFileName=_CwSctFileName_Object((1,3,6,1,4,1,9,9,236,1,1,1,5),_CwSctFileName_Type())
cwSctFileName.setMaxAccess(_G)
if mibBuilder.loadTexts:cwSctFileName.setStatus(_A)
class _CwSctFileMinorVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwSctFileMinorVersion_Type.__name__=_D
_CwSctFileMinorVersion_Object=MibTableColumn
cwSctFileMinorVersion=_CwSctFileMinorVersion_Object((1,3,6,1,4,1,9,9,236,1,1,1,6),_CwSctFileMinorVersion_Type())
cwSctFileMinorVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:cwSctFileMinorVersion.setStatus(_A)
_CwSctFileChecksum_Type=Unsigned32
_CwSctFileChecksum_Object=MibTableColumn
cwSctFileChecksum=_CwSctFileChecksum_Object((1,3,6,1,4,1,9,9,236,1,1,1,7),_CwSctFileChecksum_Type())
cwSctFileChecksum.setMaxAccess(_H)
if mibBuilder.loadTexts:cwSctFileChecksum.setStatus(_A)
class _CwSctFileDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,132))
_CwSctFileDescription_Type.__name__=_F
_CwSctFileDescription_Object=MibTableColumn
cwSctFileDescription=_CwSctFileDescription_Object((1,3,6,1,4,1,9,9,236,1,1,1,8),_CwSctFileDescription_Type())
cwSctFileDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:cwSctFileDescription.setStatus(_A)
class _CwSctFileOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),('invalid',2),('absent',3)))
_CwSctFileOperStatus_Type.__name__=_C
_CwSctFileOperStatus_Object=MibTableColumn
cwSctFileOperStatus=_CwSctFileOperStatus_Object((1,3,6,1,4,1,9,9,236,1,1,1,9),_CwSctFileOperStatus_Type())
cwSctFileOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cwSctFileOperStatus.setStatus(_A)
_CwSctFileRowStatus_Type=RowStatus
_CwSctFileRowStatus_Object=MibTableColumn
cwSctFileRowStatus=_CwSctFileRowStatus_Object((1,3,6,1,4,1,9,9,236,1,1,1,10),_CwSctFileRowStatus_Type())
cwSctFileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cwSctFileRowStatus.setStatus(_A)
_CiscoWanSctMgmtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanSctMgmtMIBConformance=_CiscoWanSctMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,236,3))
_CiscoWanSctMgmtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanSctMgmtMIBCompliances=_CiscoWanSctMgmtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,236,3,1))
_CiscoWanSctMgmtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanSctMgmtMIBGroups=_CiscoWanSctMgmtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,236,3,2))
cwSctFileMgmtObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,236,3,2,1))
cwSctFileMgmtObjectGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cwSctFileMgmtObjectGroup.setStatus(_A)
cwSctFileMgmtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,236,3,1,1))
cwSctFileMgmtMIBCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:cwSctFileMgmtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWanSctMgmtMIB':ciscoWanSctMgmtMIB,'ciscoWanSctMgmtMIBObjects':ciscoWanSctMgmtMIBObjects,'cwSctFileMgmtTable':cwSctFileMgmtTable,'cwSctFileMgmtEntry':cwSctFileMgmtEntry,_I:cwSctCardType,_J:cwSctType,_K:cwSctId,_L:cwSctMajorVersion,_M:cwSctFileName,_N:cwSctFileMinorVersion,_O:cwSctFileChecksum,_P:cwSctFileDescription,_Q:cwSctFileOperStatus,_R:cwSctFileRowStatus,'ciscoWanSctMgmtMIBConformance':ciscoWanSctMgmtMIBConformance,'ciscoWanSctMgmtMIBCompliances':ciscoWanSctMgmtMIBCompliances,'cwSctFileMgmtMIBCompliance':cwSctFileMgmtMIBCompliance,'ciscoWanSctMgmtMIBGroups':ciscoWanSctMgmtMIBGroups,_S:cwSctFileMgmtObjectGroup})