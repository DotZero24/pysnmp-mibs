_R='efpAgentInventoryNextActiveImage'
_Q='efpAgentInventoryActiveImage'
_P='efpAgentInventoryUnitImage2Md5Digest'
_O='efpAgentInventoryUnitImage1Md5Digest'
_N='efpAgentInventoryUnitImage2Timestamp'
_M='efpAgentInventoryUnitImage1Timestamp'
_L='efpAgentInventoryUnitImage2CommitHash'
_K='efpAgentInventoryUnitImage1CommitHash'
_J='efpAgentInventoryUnitEntry'
_I='image2'
_H='image1'
_G='unknown'
_F='efpInventoryUnitGroup'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='ELTEX-FASTPATH-INVENTORY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesFastpath,=mibBuilder.importSymbols('ELTEX-MES-FASTPATH-MIB','eltMesFastpath')
agentInventoryUnitEntry,=mibBuilder.importSymbols('FASTPATH-INVENTORY-MIB','agentInventoryUnitEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
eltFastpathInventoryMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,103,1))
if mibBuilder.loadTexts:eltFastpathInventoryMIB.setRevisions(('2017-02-07 00:00',))
_EfpInventoryObjects_ObjectIdentity=ObjectIdentity
efpInventoryObjects=_EfpInventoryObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,103,1,1))
_EfpInventoryGlobals_ObjectIdentity=ObjectIdentity
efpInventoryGlobals=_EfpInventoryGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,103,1,1,1))
_EfpAgentInventoryUnitTable_Object=MibTable
efpAgentInventoryUnitTable=_EfpAgentInventoryUnitTable_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1))
if mibBuilder.loadTexts:efpAgentInventoryUnitTable.setStatus(_A)
_EfpAgentInventoryUnitEntry_Object=MibTableRow
efpAgentInventoryUnitEntry=_EfpAgentInventoryUnitEntry_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1))
if mibBuilder.loadTexts:efpAgentInventoryUnitEntry.setStatus(_A)
class _EfpAgentInventoryUnitImage1CommitHash_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EfpAgentInventoryUnitImage1CommitHash_Type.__name__=_D
_EfpAgentInventoryUnitImage1CommitHash_Object=MibTableColumn
efpAgentInventoryUnitImage1CommitHash=_EfpAgentInventoryUnitImage1CommitHash_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,1),_EfpAgentInventoryUnitImage1CommitHash_Type())
efpAgentInventoryUnitImage1CommitHash.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryUnitImage1CommitHash.setStatus(_A)
class _EfpAgentInventoryUnitImage2CommitHash_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EfpAgentInventoryUnitImage2CommitHash_Type.__name__=_D
_EfpAgentInventoryUnitImage2CommitHash_Object=MibTableColumn
efpAgentInventoryUnitImage2CommitHash=_EfpAgentInventoryUnitImage2CommitHash_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,2),_EfpAgentInventoryUnitImage2CommitHash_Type())
efpAgentInventoryUnitImage2CommitHash.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryUnitImage2CommitHash.setStatus(_A)
class _EfpAgentInventoryUnitImage1Timestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EfpAgentInventoryUnitImage1Timestamp_Type.__name__=_D
_EfpAgentInventoryUnitImage1Timestamp_Object=MibTableColumn
efpAgentInventoryUnitImage1Timestamp=_EfpAgentInventoryUnitImage1Timestamp_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,3),_EfpAgentInventoryUnitImage1Timestamp_Type())
efpAgentInventoryUnitImage1Timestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryUnitImage1Timestamp.setStatus(_A)
class _EfpAgentInventoryUnitImage2Timestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EfpAgentInventoryUnitImage2Timestamp_Type.__name__=_D
_EfpAgentInventoryUnitImage2Timestamp_Object=MibTableColumn
efpAgentInventoryUnitImage2Timestamp=_EfpAgentInventoryUnitImage2Timestamp_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,4),_EfpAgentInventoryUnitImage2Timestamp_Type())
efpAgentInventoryUnitImage2Timestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryUnitImage2Timestamp.setStatus(_A)
class _EfpAgentInventoryUnitImage1Md5Digest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EfpAgentInventoryUnitImage1Md5Digest_Type.__name__=_D
_EfpAgentInventoryUnitImage1Md5Digest_Object=MibTableColumn
efpAgentInventoryUnitImage1Md5Digest=_EfpAgentInventoryUnitImage1Md5Digest_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,5),_EfpAgentInventoryUnitImage1Md5Digest_Type())
efpAgentInventoryUnitImage1Md5Digest.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryUnitImage1Md5Digest.setStatus(_A)
class _EfpAgentInventoryUnitImage2Md5Digest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_EfpAgentInventoryUnitImage2Md5Digest_Type.__name__=_D
_EfpAgentInventoryUnitImage2Md5Digest_Object=MibTableColumn
efpAgentInventoryUnitImage2Md5Digest=_EfpAgentInventoryUnitImage2Md5Digest_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,6),_EfpAgentInventoryUnitImage2Md5Digest_Type())
efpAgentInventoryUnitImage2Md5Digest.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryUnitImage2Md5Digest.setStatus(_A)
class _EfpAgentInventoryActiveImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_EfpAgentInventoryActiveImage_Type.__name__=_E
_EfpAgentInventoryActiveImage_Object=MibTableColumn
efpAgentInventoryActiveImage=_EfpAgentInventoryActiveImage_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,7),_EfpAgentInventoryActiveImage_Type())
efpAgentInventoryActiveImage.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryActiveImage.setStatus(_A)
class _EfpAgentInventoryNextActiveImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_EfpAgentInventoryNextActiveImage_Type.__name__=_E
_EfpAgentInventoryNextActiveImage_Object=MibTableColumn
efpAgentInventoryNextActiveImage=_EfpAgentInventoryNextActiveImage_Object((1,3,6,1,4,1,35265,1,103,1,1,1,1,1,8),_EfpAgentInventoryNextActiveImage_Type())
efpAgentInventoryNextActiveImage.setMaxAccess(_C)
if mibBuilder.loadTexts:efpAgentInventoryNextActiveImage.setStatus(_A)
_EfpInventoryNotifications_ObjectIdentity=ObjectIdentity
efpInventoryNotifications=_EfpInventoryNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,103,1,2))
_EfpInventoryNotificationsPrefix_ObjectIdentity=ObjectIdentity
efpInventoryNotificationsPrefix=_EfpInventoryNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,103,1,2,0))
_EfpInventoryConformance_ObjectIdentity=ObjectIdentity
efpInventoryConformance=_EfpInventoryConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,103,1,3))
_EfpInventoryCompliances_ObjectIdentity=ObjectIdentity
efpInventoryCompliances=_EfpInventoryCompliances_ObjectIdentity((1,3,6,1,4,1,35265,1,103,1,3,1))
_EfpInventoryGroups_ObjectIdentity=ObjectIdentity
efpInventoryGroups=_EfpInventoryGroups_ObjectIdentity((1,3,6,1,4,1,35265,1,103,1,3,2))
agentInventoryUnitEntry.registerAugmentions((_B,_J))
efpAgentInventoryUnitEntry.setIndexNames(*agentInventoryUnitEntry.getIndexNames())
efpInventoryUnitGroup=ObjectGroup((1,3,6,1,4,1,35265,1,103,1,3,2,2))
efpInventoryUnitGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:efpInventoryUnitGroup.setStatus(_A)
efpInventoryCompliance=ModuleCompliance((1,3,6,1,4,1,35265,1,103,1,3,1,1))
efpInventoryCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:efpInventoryCompliance.setStatus('obsolete')
efpFastPathInventoryMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,35265,1,103,1,3,1,2))
efpFastPathInventoryMIBCompliance2.setObjects((_B,_F))
if mibBuilder.loadTexts:efpFastPathInventoryMIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltFastpathInventoryMIB':eltFastpathInventoryMIB,'efpInventoryObjects':efpInventoryObjects,'efpInventoryGlobals':efpInventoryGlobals,'efpAgentInventoryUnitTable':efpAgentInventoryUnitTable,_J:efpAgentInventoryUnitEntry,_K:efpAgentInventoryUnitImage1CommitHash,_L:efpAgentInventoryUnitImage2CommitHash,_M:efpAgentInventoryUnitImage1Timestamp,_N:efpAgentInventoryUnitImage2Timestamp,_O:efpAgentInventoryUnitImage1Md5Digest,_P:efpAgentInventoryUnitImage2Md5Digest,_Q:efpAgentInventoryActiveImage,_R:efpAgentInventoryNextActiveImage,'efpInventoryNotifications':efpInventoryNotifications,'efpInventoryNotificationsPrefix':efpInventoryNotificationsPrefix,'efpInventoryConformance':efpInventoryConformance,'efpInventoryCompliances':efpInventoryCompliances,'efpInventoryCompliance':efpInventoryCompliance,'efpFastPathInventoryMIBCompliance2':efpFastPathInventoryMIBCompliance2,'efpInventoryGroups':efpInventoryGroups,_F:efpInventoryUnitGroup})