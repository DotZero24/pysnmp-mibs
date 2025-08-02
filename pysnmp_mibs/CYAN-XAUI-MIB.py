_O='cyanXauiObjectGroup'
_N='cyanXauiSecServState'
_M='cyanXauiPortSpeedMbps'
_L='cyanXauiOperStateQual'
_K='cyanXauiOperState'
_J='cyanXauiAutoinserviceSoakTimeSec'
_I='cyanXauiAdminState'
_H='cyanXauiXauiId'
_G='cyanXauiModuleId'
_F='cyanXauiShelfId'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='CYAN-XAUI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyanEntityModules,=mibBuilder.importSymbols('CYAN-MIB','cyanEntityModules')
CyanAdminStateTc,CyanOpStateQualTc,CyanOpStateTc,CyanSecServiceStateTc=mibBuilder.importSymbols('CYAN-TC-MIB','CyanAdminStateTc','CyanOpStateQualTc','CyanOpStateTc','CyanSecServiceStateTc')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyanXauiModule=ModuleIdentity((1,3,6,1,4,1,28533,5,30,170))
if mibBuilder.loadTexts:cyanXauiModule.setRevisions(('2014-12-07 05:45',))
_CyanXauiMibObjects_ObjectIdentity=ObjectIdentity
cyanXauiMibObjects=_CyanXauiMibObjects_ObjectIdentity((1,3,6,1,4,1,28533,5,30,170,1))
_CyanXauiTable_Object=MibTable
cyanXauiTable=_CyanXauiTable_Object((1,3,6,1,4,1,28533,5,30,170,1,1))
if mibBuilder.loadTexts:cyanXauiTable.setStatus(_A)
_CyanXauiEntry_Object=MibTableRow
cyanXauiEntry=_CyanXauiEntry_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1))
cyanXauiEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cyanXauiEntry.setStatus(_A)
class _CyanXauiShelfId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CyanXauiShelfId_Type.__name__=_E
_CyanXauiShelfId_Object=MibTableColumn
cyanXauiShelfId=_CyanXauiShelfId_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,1),_CyanXauiShelfId_Type())
cyanXauiShelfId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanXauiShelfId.setStatus(_A)
_CyanXauiModuleId_Type=Unsigned32
_CyanXauiModuleId_Object=MibTableColumn
cyanXauiModuleId=_CyanXauiModuleId_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,2),_CyanXauiModuleId_Type())
cyanXauiModuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanXauiModuleId.setStatus(_A)
_CyanXauiXauiId_Type=Unsigned32
_CyanXauiXauiId_Object=MibTableColumn
cyanXauiXauiId=_CyanXauiXauiId_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,3),_CyanXauiXauiId_Type())
cyanXauiXauiId.setMaxAccess(_D)
if mibBuilder.loadTexts:cyanXauiXauiId.setStatus(_A)
_CyanXauiAdminState_Type=CyanAdminStateTc
_CyanXauiAdminState_Object=MibTableColumn
cyanXauiAdminState=_CyanXauiAdminState_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,4),_CyanXauiAdminState_Type())
cyanXauiAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanXauiAdminState.setStatus(_A)
_CyanXauiAutoinserviceSoakTimeSec_Type=Integer32
_CyanXauiAutoinserviceSoakTimeSec_Object=MibTableColumn
cyanXauiAutoinserviceSoakTimeSec=_CyanXauiAutoinserviceSoakTimeSec_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,5),_CyanXauiAutoinserviceSoakTimeSec_Type())
cyanXauiAutoinserviceSoakTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanXauiAutoinserviceSoakTimeSec.setStatus(_A)
_CyanXauiOperState_Type=CyanOpStateTc
_CyanXauiOperState_Object=MibTableColumn
cyanXauiOperState=_CyanXauiOperState_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,6),_CyanXauiOperState_Type())
cyanXauiOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanXauiOperState.setStatus(_A)
_CyanXauiOperStateQual_Type=CyanOpStateQualTc
_CyanXauiOperStateQual_Object=MibTableColumn
cyanXauiOperStateQual=_CyanXauiOperStateQual_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,7),_CyanXauiOperStateQual_Type())
cyanXauiOperStateQual.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanXauiOperStateQual.setStatus(_A)
_CyanXauiPortSpeedMbps_Type=Unsigned32
_CyanXauiPortSpeedMbps_Object=MibTableColumn
cyanXauiPortSpeedMbps=_CyanXauiPortSpeedMbps_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,8),_CyanXauiPortSpeedMbps_Type())
cyanXauiPortSpeedMbps.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanXauiPortSpeedMbps.setStatus(_A)
_CyanXauiSecServState_Type=CyanSecServiceStateTc
_CyanXauiSecServState_Object=MibTableColumn
cyanXauiSecServState=_CyanXauiSecServState_Object((1,3,6,1,4,1,28533,5,30,170,1,1,1,9),_CyanXauiSecServState_Type())
cyanXauiSecServState.setMaxAccess(_C)
if mibBuilder.loadTexts:cyanXauiSecServState.setStatus(_A)
cyanXauiObjectGroup=ObjectGroup((1,3,6,1,4,1,28533,5,30,170,20))
cyanXauiObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cyanXauiObjectGroup.setStatus(_A)
cyanXauiCompliance=ModuleCompliance((1,3,6,1,4,1,28533,5,30,170,30))
cyanXauiCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:cyanXauiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cyanXauiModule':cyanXauiModule,'cyanXauiMibObjects':cyanXauiMibObjects,'cyanXauiTable':cyanXauiTable,'cyanXauiEntry':cyanXauiEntry,_F:cyanXauiShelfId,_G:cyanXauiModuleId,_H:cyanXauiXauiId,_I:cyanXauiAdminState,_J:cyanXauiAutoinserviceSoakTimeSec,_K:cyanXauiOperState,_L:cyanXauiOperStateQual,_M:cyanXauiPortSpeedMbps,_N:cyanXauiSecServState,_O:cyanXauiObjectGroup,'cyanXauiCompliance':cyanXauiCompliance})