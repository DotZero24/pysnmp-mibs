_W='csrlLocalRateLimiterGroup'
_V='csrlGlobalRateLimiterGroup'
_U='csrlRateLimiterClassGroup'
_T='csrlLocalRateLimiterTotal'
_S='csrlLocalRateLimiterDropped'
_R='csrlLocalRateLimiterAllowed'
_Q='csrlLocalRateLimiterConfigured'
_P='csrlGlobalRateLimiterTotal'
_O='csrlGlobalRateLimiterDropped'
_N='csrlGlobalRateLimiterAllowed'
_M='csrlGlobalRateLimiterConfigured'
_L='csrlRateLimiterClassDescr'
_K='packets per second'
_J='read-write'
_I='Unsigned32'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='Integer32'
_E='csrlRateLimiterClassId'
_D='packets'
_C='read-only'
_B='CISCO-SWITCH-RATE-LIMITER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSwitchRateLimiterMIB=ModuleIdentity((1,3,6,1,4,1,9,9,773))
if mibBuilder.loadTexts:ciscoSwitchRateLimiterMIB.setRevisions(('2011-05-16 00:00',))
_CiscoSwitchRateLimiterMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSwitchRateLimiterMIBNotifs=_CiscoSwitchRateLimiterMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,773,0))
_CiscoSwitchRateLimiterMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchRateLimiterMIBObjects=_CiscoSwitchRateLimiterMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,773,1))
_CsrlRateLimiterInfo_ObjectIdentity=ObjectIdentity
csrlRateLimiterInfo=_CsrlRateLimiterInfo_ObjectIdentity((1,3,6,1,4,1,9,9,773,1,1))
_CsrlRateLimiterClassTable_Object=MibTable
csrlRateLimiterClassTable=_CsrlRateLimiterClassTable_Object((1,3,6,1,4,1,9,9,773,1,1,1))
if mibBuilder.loadTexts:csrlRateLimiterClassTable.setStatus(_A)
_CsrlRateLimiterClassEntry_Object=MibTableRow
csrlRateLimiterClassEntry=_CsrlRateLimiterClassEntry_Object((1,3,6,1,4,1,9,9,773,1,1,1,1))
csrlRateLimiterClassEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:csrlRateLimiterClassEntry.setStatus(_A)
class _CsrlRateLimiterClassId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CsrlRateLimiterClassId_Type.__name__=_I
_CsrlRateLimiterClassId_Object=MibTableColumn
csrlRateLimiterClassId=_CsrlRateLimiterClassId_Object((1,3,6,1,4,1,9,9,773,1,1,1,1,1),_CsrlRateLimiterClassId_Type())
csrlRateLimiterClassId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:csrlRateLimiterClassId.setStatus(_A)
_CsrlRateLimiterClassDescr_Type=SnmpAdminString
_CsrlRateLimiterClassDescr_Object=MibTableColumn
csrlRateLimiterClassDescr=_CsrlRateLimiterClassDescr_Object((1,3,6,1,4,1,9,9,773,1,1,1,1,2),_CsrlRateLimiterClassDescr_Type())
csrlRateLimiterClassDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:csrlRateLimiterClassDescr.setStatus(_A)
_CsrlGlobalRateLimiter_ObjectIdentity=ObjectIdentity
csrlGlobalRateLimiter=_CsrlGlobalRateLimiter_ObjectIdentity((1,3,6,1,4,1,9,9,773,1,2))
_CsrlGlobalRateLimiterTable_Object=MibTable
csrlGlobalRateLimiterTable=_CsrlGlobalRateLimiterTable_Object((1,3,6,1,4,1,9,9,773,1,2,1))
if mibBuilder.loadTexts:csrlGlobalRateLimiterTable.setStatus(_A)
_CsrlGlobalRateLimiterEntry_Object=MibTableRow
csrlGlobalRateLimiterEntry=_CsrlGlobalRateLimiterEntry_Object((1,3,6,1,4,1,9,9,773,1,2,1,1))
csrlGlobalRateLimiterEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:csrlGlobalRateLimiterEntry.setStatus(_A)
class _CsrlGlobalRateLimiterConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_CsrlGlobalRateLimiterConfigured_Type.__name__=_F
_CsrlGlobalRateLimiterConfigured_Object=MibTableColumn
csrlGlobalRateLimiterConfigured=_CsrlGlobalRateLimiterConfigured_Object((1,3,6,1,4,1,9,9,773,1,2,1,1,1),_CsrlGlobalRateLimiterConfigured_Type())
csrlGlobalRateLimiterConfigured.setMaxAccess(_J)
if mibBuilder.loadTexts:csrlGlobalRateLimiterConfigured.setStatus(_A)
if mibBuilder.loadTexts:csrlGlobalRateLimiterConfigured.setUnits(_K)
_CsrlGlobalRateLimiterAllowed_Type=Counter64
_CsrlGlobalRateLimiterAllowed_Object=MibTableColumn
csrlGlobalRateLimiterAllowed=_CsrlGlobalRateLimiterAllowed_Object((1,3,6,1,4,1,9,9,773,1,2,1,1,2),_CsrlGlobalRateLimiterAllowed_Type())
csrlGlobalRateLimiterAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:csrlGlobalRateLimiterAllowed.setStatus(_A)
if mibBuilder.loadTexts:csrlGlobalRateLimiterAllowed.setUnits(_D)
_CsrlGlobalRateLimiterDropped_Type=Counter64
_CsrlGlobalRateLimiterDropped_Object=MibTableColumn
csrlGlobalRateLimiterDropped=_CsrlGlobalRateLimiterDropped_Object((1,3,6,1,4,1,9,9,773,1,2,1,1,3),_CsrlGlobalRateLimiterDropped_Type())
csrlGlobalRateLimiterDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:csrlGlobalRateLimiterDropped.setStatus(_A)
if mibBuilder.loadTexts:csrlGlobalRateLimiterDropped.setUnits(_D)
_CsrlGlobalRateLimiterTotal_Type=Counter64
_CsrlGlobalRateLimiterTotal_Object=MibTableColumn
csrlGlobalRateLimiterTotal=_CsrlGlobalRateLimiterTotal_Object((1,3,6,1,4,1,9,9,773,1,2,1,1,4),_CsrlGlobalRateLimiterTotal_Type())
csrlGlobalRateLimiterTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:csrlGlobalRateLimiterTotal.setStatus(_A)
if mibBuilder.loadTexts:csrlGlobalRateLimiterTotal.setUnits(_D)
_CsrlLocalRateLimiter_ObjectIdentity=ObjectIdentity
csrlLocalRateLimiter=_CsrlLocalRateLimiter_ObjectIdentity((1,3,6,1,4,1,9,9,773,1,3))
_CsrlLocalRateLimiterTable_Object=MibTable
csrlLocalRateLimiterTable=_CsrlLocalRateLimiterTable_Object((1,3,6,1,4,1,9,9,773,1,3,1))
if mibBuilder.loadTexts:csrlLocalRateLimiterTable.setStatus(_A)
_CsrlLocalRateLimiterEntry_Object=MibTableRow
csrlLocalRateLimiterEntry=_CsrlLocalRateLimiterEntry_Object((1,3,6,1,4,1,9,9,773,1,3,1,1))
csrlLocalRateLimiterEntry.setIndexNames((0,_G,_H),(0,_B,_E))
if mibBuilder.loadTexts:csrlLocalRateLimiterEntry.setStatus(_A)
class _CsrlLocalRateLimiterConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,-2),ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_CsrlLocalRateLimiterConfigured_Type.__name__=_F
_CsrlLocalRateLimiterConfigured_Object=MibTableColumn
csrlLocalRateLimiterConfigured=_CsrlLocalRateLimiterConfigured_Object((1,3,6,1,4,1,9,9,773,1,3,1,1,1),_CsrlLocalRateLimiterConfigured_Type())
csrlLocalRateLimiterConfigured.setMaxAccess(_J)
if mibBuilder.loadTexts:csrlLocalRateLimiterConfigured.setStatus(_A)
if mibBuilder.loadTexts:csrlLocalRateLimiterConfigured.setUnits(_K)
_CsrlLocalRateLimiterAllowed_Type=Counter64
_CsrlLocalRateLimiterAllowed_Object=MibTableColumn
csrlLocalRateLimiterAllowed=_CsrlLocalRateLimiterAllowed_Object((1,3,6,1,4,1,9,9,773,1,3,1,1,2),_CsrlLocalRateLimiterAllowed_Type())
csrlLocalRateLimiterAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:csrlLocalRateLimiterAllowed.setStatus(_A)
if mibBuilder.loadTexts:csrlLocalRateLimiterAllowed.setUnits(_D)
_CsrlLocalRateLimiterDropped_Type=Counter64
_CsrlLocalRateLimiterDropped_Object=MibTableColumn
csrlLocalRateLimiterDropped=_CsrlLocalRateLimiterDropped_Object((1,3,6,1,4,1,9,9,773,1,3,1,1,3),_CsrlLocalRateLimiterDropped_Type())
csrlLocalRateLimiterDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:csrlLocalRateLimiterDropped.setStatus(_A)
if mibBuilder.loadTexts:csrlLocalRateLimiterDropped.setUnits(_D)
_CsrlLocalRateLimiterTotal_Type=Counter64
_CsrlLocalRateLimiterTotal_Object=MibTableColumn
csrlLocalRateLimiterTotal=_CsrlLocalRateLimiterTotal_Object((1,3,6,1,4,1,9,9,773,1,3,1,1,4),_CsrlLocalRateLimiterTotal_Type())
csrlLocalRateLimiterTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:csrlLocalRateLimiterTotal.setStatus(_A)
if mibBuilder.loadTexts:csrlLocalRateLimiterTotal.setUnits(_D)
_CiscoSwitchRateLimiterMIBConform_ObjectIdentity=ObjectIdentity
ciscoSwitchRateLimiterMIBConform=_CiscoSwitchRateLimiterMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,773,2))
_CsrlMIBCompliances_ObjectIdentity=ObjectIdentity
csrlMIBCompliances=_CsrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,773,2,1))
_CsrlMIBGroups_ObjectIdentity=ObjectIdentity
csrlMIBGroups=_CsrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,773,2,2))
csrlRateLimiterClassGroup=ObjectGroup((1,3,6,1,4,1,9,9,773,2,2,1))
csrlRateLimiterClassGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:csrlRateLimiterClassGroup.setStatus(_A)
csrlGlobalRateLimiterGroup=ObjectGroup((1,3,6,1,4,1,9,9,773,2,2,2))
csrlGlobalRateLimiterGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:csrlGlobalRateLimiterGroup.setStatus(_A)
csrlLocalRateLimiterGroup=ObjectGroup((1,3,6,1,4,1,9,9,773,2,2,3))
csrlLocalRateLimiterGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:csrlLocalRateLimiterGroup.setStatus(_A)
csrlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,773,2,1,1))
csrlMIBCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:csrlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSwitchRateLimiterMIB':ciscoSwitchRateLimiterMIB,'ciscoSwitchRateLimiterMIBNotifs':ciscoSwitchRateLimiterMIBNotifs,'ciscoSwitchRateLimiterMIBObjects':ciscoSwitchRateLimiterMIBObjects,'csrlRateLimiterInfo':csrlRateLimiterInfo,'csrlRateLimiterClassTable':csrlRateLimiterClassTable,'csrlRateLimiterClassEntry':csrlRateLimiterClassEntry,_E:csrlRateLimiterClassId,_L:csrlRateLimiterClassDescr,'csrlGlobalRateLimiter':csrlGlobalRateLimiter,'csrlGlobalRateLimiterTable':csrlGlobalRateLimiterTable,'csrlGlobalRateLimiterEntry':csrlGlobalRateLimiterEntry,_M:csrlGlobalRateLimiterConfigured,_N:csrlGlobalRateLimiterAllowed,_O:csrlGlobalRateLimiterDropped,_P:csrlGlobalRateLimiterTotal,'csrlLocalRateLimiter':csrlLocalRateLimiter,'csrlLocalRateLimiterTable':csrlLocalRateLimiterTable,'csrlLocalRateLimiterEntry':csrlLocalRateLimiterEntry,_Q:csrlLocalRateLimiterConfigured,_R:csrlLocalRateLimiterAllowed,_S:csrlLocalRateLimiterDropped,_T:csrlLocalRateLimiterTotal,'ciscoSwitchRateLimiterMIBConform':ciscoSwitchRateLimiterMIBConform,'csrlMIBCompliances':csrlMIBCompliances,'csrlMIBCompliance':csrlMIBCompliance,'csrlMIBGroups':csrlMIBGroups,_U:csrlRateLimiterClassGroup,_V:csrlGlobalRateLimiterGroup,_W:csrlLocalRateLimiterGroup})