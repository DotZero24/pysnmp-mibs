_Q='oaLdPortsCntrGroup'
_P='oaLdPortsCntrOutOctets'
_O='oaLdPortsCntrInOctets'
_N='oaLdPortsCntrOutPkts'
_M='oaLdPortsCntrInPkts'
_L='oaLdPortsCntrCodeViols'
_K='oaLdPortsCntrOutRateBits'
_J='oaLdPortsCntrInRateBits'
_I='oaLdPortsCntrCrcErrs'
_H='oaLdPortsCntrSyncErrs'
_G='not-accessible'
_F='oaLdPortsCntrPortNumber'
_E='oaLdPortsCntrSlotNumber'
_D='Integer32'
_C='read-only'
_B='OADWDM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oaLambdaDriver=ModuleIdentity((1,3,6,1,4,1,6926,1,41))
if mibBuilder.loadTexts:oaLambdaDriver.setRevisions(('2009-06-28 00:00',))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaLdPortsCntr_ObjectIdentity=ObjectIdentity
oaLdPortsCntr=_OaLdPortsCntr_ObjectIdentity((1,3,6,1,4,1,6926,1,41,10))
_OaLdPortsCntrTable_Object=MibTable
oaLdPortsCntrTable=_OaLdPortsCntrTable_Object((1,3,6,1,4,1,6926,1,41,10,2))
if mibBuilder.loadTexts:oaLdPortsCntrTable.setStatus(_A)
_OaLdPortsCntrEntry_Object=MibTableRow
oaLdPortsCntrEntry=_OaLdPortsCntrEntry_Object((1,3,6,1,4,1,6926,1,41,10,2,1))
oaLdPortsCntrEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:oaLdPortsCntrEntry.setStatus(_A)
class _OaLdPortsCntrSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_OaLdPortsCntrSlotNumber_Type.__name__=_D
_OaLdPortsCntrSlotNumber_Object=MibTableColumn
oaLdPortsCntrSlotNumber=_OaLdPortsCntrSlotNumber_Object((1,3,6,1,4,1,6926,1,41,10,2,1,1),_OaLdPortsCntrSlotNumber_Type())
oaLdPortsCntrSlotNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:oaLdPortsCntrSlotNumber.setStatus(_A)
class _OaLdPortsCntrPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_OaLdPortsCntrPortNumber_Type.__name__=_D
_OaLdPortsCntrPortNumber_Object=MibTableColumn
oaLdPortsCntrPortNumber=_OaLdPortsCntrPortNumber_Object((1,3,6,1,4,1,6926,1,41,10,2,1,2),_OaLdPortsCntrPortNumber_Type())
oaLdPortsCntrPortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:oaLdPortsCntrPortNumber.setStatus(_A)
_OaLdPortsCntrSyncErrs_Type=Counter32
_OaLdPortsCntrSyncErrs_Object=MibTableColumn
oaLdPortsCntrSyncErrs=_OaLdPortsCntrSyncErrs_Object((1,3,6,1,4,1,6926,1,41,10,2,1,3),_OaLdPortsCntrSyncErrs_Type())
oaLdPortsCntrSyncErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrSyncErrs.setStatus(_A)
_OaLdPortsCntrCrcErrs_Type=Counter32
_OaLdPortsCntrCrcErrs_Object=MibTableColumn
oaLdPortsCntrCrcErrs=_OaLdPortsCntrCrcErrs_Object((1,3,6,1,4,1,6926,1,41,10,2,1,4),_OaLdPortsCntrCrcErrs_Type())
oaLdPortsCntrCrcErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrCrcErrs.setStatus(_A)
_OaLdPortsCntrInRateBits_Type=Integer32
_OaLdPortsCntrInRateBits_Object=MibTableColumn
oaLdPortsCntrInRateBits=_OaLdPortsCntrInRateBits_Object((1,3,6,1,4,1,6926,1,41,10,2,1,5),_OaLdPortsCntrInRateBits_Type())
oaLdPortsCntrInRateBits.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrInRateBits.setStatus(_A)
_OaLdPortsCntrOutRateBits_Type=Integer32
_OaLdPortsCntrOutRateBits_Object=MibTableColumn
oaLdPortsCntrOutRateBits=_OaLdPortsCntrOutRateBits_Object((1,3,6,1,4,1,6926,1,41,10,2,1,6),_OaLdPortsCntrOutRateBits_Type())
oaLdPortsCntrOutRateBits.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrOutRateBits.setStatus(_A)
_OaLdPortsCntrCodeViols_Type=Counter32
_OaLdPortsCntrCodeViols_Object=MibTableColumn
oaLdPortsCntrCodeViols=_OaLdPortsCntrCodeViols_Object((1,3,6,1,4,1,6926,1,41,10,2,1,7),_OaLdPortsCntrCodeViols_Type())
oaLdPortsCntrCodeViols.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrCodeViols.setStatus(_A)
_OaLdPortsCntrInPkts_Type=Counter64
_OaLdPortsCntrInPkts_Object=MibTableColumn
oaLdPortsCntrInPkts=_OaLdPortsCntrInPkts_Object((1,3,6,1,4,1,6926,1,41,10,2,1,8),_OaLdPortsCntrInPkts_Type())
oaLdPortsCntrInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrInPkts.setStatus(_A)
_OaLdPortsCntrOutPkts_Type=Counter64
_OaLdPortsCntrOutPkts_Object=MibTableColumn
oaLdPortsCntrOutPkts=_OaLdPortsCntrOutPkts_Object((1,3,6,1,4,1,6926,1,41,10,2,1,9),_OaLdPortsCntrOutPkts_Type())
oaLdPortsCntrOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrOutPkts.setStatus(_A)
_OaLdPortsCntrInOctets_Type=Counter64
_OaLdPortsCntrInOctets_Object=MibTableColumn
oaLdPortsCntrInOctets=_OaLdPortsCntrInOctets_Object((1,3,6,1,4,1,6926,1,41,10,2,1,10),_OaLdPortsCntrInOctets_Type())
oaLdPortsCntrInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrInOctets.setStatus(_A)
_OaLdPortsCntrOutOctets_Type=Counter64
_OaLdPortsCntrOutOctets_Object=MibTableColumn
oaLdPortsCntrOutOctets=_OaLdPortsCntrOutOctets_Object((1,3,6,1,4,1,6926,1,41,10,2,1,11),_OaLdPortsCntrOutOctets_Type())
oaLdPortsCntrOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdPortsCntrOutOctets.setStatus(_A)
_OaLdPortsCntrConformance_ObjectIdentity=ObjectIdentity
oaLdPortsCntrConformance=_OaLdPortsCntrConformance_ObjectIdentity((1,3,6,1,4,1,6926,1,41,100))
_OaLdPortsCntrGroups_ObjectIdentity=ObjectIdentity
oaLdPortsCntrGroups=_OaLdPortsCntrGroups_ObjectIdentity((1,3,6,1,4,1,6926,1,41,100,1))
_OaLdPortsCntrCompliances_ObjectIdentity=ObjectIdentity
oaLdPortsCntrCompliances=_OaLdPortsCntrCompliances_ObjectIdentity((1,3,6,1,4,1,6926,1,41,100,2))
oaLdPortsCntrGroup=ObjectGroup((1,3,6,1,4,1,6926,1,41,100,1,1))
oaLdPortsCntrGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:oaLdPortsCntrGroup.setStatus(_A)
oaLdPortsCntrCompliance=ModuleCompliance((1,3,6,1,4,1,6926,1,41,100,2,1))
oaLdPortsCntrCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:oaLdPortsCntrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oaccess':oaccess,'oaManagement':oaManagement,'oaLambdaDriver':oaLambdaDriver,'oaLdPortsCntr':oaLdPortsCntr,'oaLdPortsCntrTable':oaLdPortsCntrTable,'oaLdPortsCntrEntry':oaLdPortsCntrEntry,_E:oaLdPortsCntrSlotNumber,_F:oaLdPortsCntrPortNumber,_H:oaLdPortsCntrSyncErrs,_I:oaLdPortsCntrCrcErrs,_J:oaLdPortsCntrInRateBits,_K:oaLdPortsCntrOutRateBits,_L:oaLdPortsCntrCodeViols,_M:oaLdPortsCntrInPkts,_N:oaLdPortsCntrOutPkts,_O:oaLdPortsCntrInOctets,_P:oaLdPortsCntrOutOctets,'oaLdPortsCntrConformance':oaLdPortsCntrConformance,'oaLdPortsCntrGroups':oaLdPortsCntrGroups,_Q:oaLdPortsCntrGroup,'oaLdPortsCntrCompliances':oaLdPortsCntrCompliances,'oaLdPortsCntrCompliance':oaLdPortsCntrCompliance})