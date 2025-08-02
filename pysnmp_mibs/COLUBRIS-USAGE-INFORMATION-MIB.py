_S='colubrisUsageInformationMIBGroup'
_R='coUsInfoStorageUseTemporary'
_Q='coUsInfoStorageUsePermanent'
_P='coUsInfoRamCached'
_O='coUsInfoRamBuffer'
_N='coUsInfoRamFree'
_M='coUsInfoRamTotal'
_L='coUsInfoCpuUse20Sec'
_K='coUsInfoCpuUse10Sec'
_J='coUsInfoCpuUse5Sec'
_I='coUsInfoCpuUseNow'
_H='coUsInfoLoadAverage15Min'
_G='coUsInfoLoadAverage5Min'
_F='coUsInfoLoadAverage1Min'
_E='coUsInfoUpTime'
_D='Kb'
_C='read-only'
_B='COLUBRIS-USAGE-INFORMATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisUsageInformationMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,21))
_ColubrisUsageInformationMIBObjects_ObjectIdentity=ObjectIdentity
colubrisUsageInformationMIBObjects=_ColubrisUsageInformationMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,21,1))
_CoUsageInformationGroup_ObjectIdentity=ObjectIdentity
coUsageInformationGroup=_CoUsageInformationGroup_ObjectIdentity((1,3,6,1,4,1,8744,5,21,1,1))
_CoUsInfoUpTime_Type=TimeTicks
_CoUsInfoUpTime_Object=MibScalar
coUsInfoUpTime=_CoUsInfoUpTime_Object((1,3,6,1,4,1,8744,5,21,1,1,1),_CoUsInfoUpTime_Type())
coUsInfoUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoUpTime.setStatus(_A)
_CoUsInfoLoadAverage1Min_Type=Unsigned32
_CoUsInfoLoadAverage1Min_Object=MibScalar
coUsInfoLoadAverage1Min=_CoUsInfoLoadAverage1Min_Object((1,3,6,1,4,1,8744,5,21,1,1,2),_CoUsInfoLoadAverage1Min_Type())
coUsInfoLoadAverage1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoLoadAverage1Min.setStatus(_A)
_CoUsInfoLoadAverage5Min_Type=Unsigned32
_CoUsInfoLoadAverage5Min_Object=MibScalar
coUsInfoLoadAverage5Min=_CoUsInfoLoadAverage5Min_Object((1,3,6,1,4,1,8744,5,21,1,1,3),_CoUsInfoLoadAverage5Min_Type())
coUsInfoLoadAverage5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoLoadAverage5Min.setStatus(_A)
_CoUsInfoLoadAverage15Min_Type=Unsigned32
_CoUsInfoLoadAverage15Min_Object=MibScalar
coUsInfoLoadAverage15Min=_CoUsInfoLoadAverage15Min_Object((1,3,6,1,4,1,8744,5,21,1,1,4),_CoUsInfoLoadAverage15Min_Type())
coUsInfoLoadAverage15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoLoadAverage15Min.setStatus(_A)
_CoUsInfoCpuUseNow_Type=Unsigned32
_CoUsInfoCpuUseNow_Object=MibScalar
coUsInfoCpuUseNow=_CoUsInfoCpuUseNow_Object((1,3,6,1,4,1,8744,5,21,1,1,5),_CoUsInfoCpuUseNow_Type())
coUsInfoCpuUseNow.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoCpuUseNow.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoCpuUseNow.setUnits('%')
_CoUsInfoCpuUse5Sec_Type=Unsigned32
_CoUsInfoCpuUse5Sec_Object=MibScalar
coUsInfoCpuUse5Sec=_CoUsInfoCpuUse5Sec_Object((1,3,6,1,4,1,8744,5,21,1,1,6),_CoUsInfoCpuUse5Sec_Type())
coUsInfoCpuUse5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoCpuUse5Sec.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoCpuUse5Sec.setUnits('%')
_CoUsInfoCpuUse10Sec_Type=Unsigned32
_CoUsInfoCpuUse10Sec_Object=MibScalar
coUsInfoCpuUse10Sec=_CoUsInfoCpuUse10Sec_Object((1,3,6,1,4,1,8744,5,21,1,1,7),_CoUsInfoCpuUse10Sec_Type())
coUsInfoCpuUse10Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoCpuUse10Sec.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoCpuUse10Sec.setUnits('%')
_CoUsInfoCpuUse20Sec_Type=Unsigned32
_CoUsInfoCpuUse20Sec_Object=MibScalar
coUsInfoCpuUse20Sec=_CoUsInfoCpuUse20Sec_Object((1,3,6,1,4,1,8744,5,21,1,1,8),_CoUsInfoCpuUse20Sec_Type())
coUsInfoCpuUse20Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoCpuUse20Sec.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoCpuUse20Sec.setUnits('%')
_CoUsInfoRamTotal_Type=Unsigned32
_CoUsInfoRamTotal_Object=MibScalar
coUsInfoRamTotal=_CoUsInfoRamTotal_Object((1,3,6,1,4,1,8744,5,21,1,1,9),_CoUsInfoRamTotal_Type())
coUsInfoRamTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoRamTotal.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoRamTotal.setUnits(_D)
_CoUsInfoRamFree_Type=Unsigned32
_CoUsInfoRamFree_Object=MibScalar
coUsInfoRamFree=_CoUsInfoRamFree_Object((1,3,6,1,4,1,8744,5,21,1,1,10),_CoUsInfoRamFree_Type())
coUsInfoRamFree.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoRamFree.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoRamFree.setUnits(_D)
_CoUsInfoRamBuffer_Type=Unsigned32
_CoUsInfoRamBuffer_Object=MibScalar
coUsInfoRamBuffer=_CoUsInfoRamBuffer_Object((1,3,6,1,4,1,8744,5,21,1,1,11),_CoUsInfoRamBuffer_Type())
coUsInfoRamBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoRamBuffer.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoRamBuffer.setUnits(_D)
_CoUsInfoRamCached_Type=Unsigned32
_CoUsInfoRamCached_Object=MibScalar
coUsInfoRamCached=_CoUsInfoRamCached_Object((1,3,6,1,4,1,8744,5,21,1,1,12),_CoUsInfoRamCached_Type())
coUsInfoRamCached.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoRamCached.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoRamCached.setUnits(_D)
_CoUsInfoStorageUsePermanent_Type=Unsigned32
_CoUsInfoStorageUsePermanent_Object=MibScalar
coUsInfoStorageUsePermanent=_CoUsInfoStorageUsePermanent_Object((1,3,6,1,4,1,8744,5,21,1,1,13),_CoUsInfoStorageUsePermanent_Type())
coUsInfoStorageUsePermanent.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoStorageUsePermanent.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoStorageUsePermanent.setUnits('%')
_CoUsInfoStorageUseTemporary_Type=Unsigned32
_CoUsInfoStorageUseTemporary_Object=MibScalar
coUsInfoStorageUseTemporary=_CoUsInfoStorageUseTemporary_Object((1,3,6,1,4,1,8744,5,21,1,1,14),_CoUsInfoStorageUseTemporary_Type())
coUsInfoStorageUseTemporary.setMaxAccess(_C)
if mibBuilder.loadTexts:coUsInfoStorageUseTemporary.setStatus(_A)
if mibBuilder.loadTexts:coUsInfoStorageUseTemporary.setUnits('%')
_ColubrisUsageInformationMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisUsageInformationMIBNotificationPrefix=_ColubrisUsageInformationMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,21,2))
_ColubrisUsageInformationMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisUsageInformationMIBNotifications=_ColubrisUsageInformationMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,21,2,0))
_ColubrisUsageInformationMIBConformance_ObjectIdentity=ObjectIdentity
colubrisUsageInformationMIBConformance=_ColubrisUsageInformationMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,21,3))
_ColubrisUsageInformationMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisUsageInformationMIBCompliances=_ColubrisUsageInformationMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,21,3,1))
_ColubrisUsageInformationMIBGroups_ObjectIdentity=ObjectIdentity
colubrisUsageInformationMIBGroups=_ColubrisUsageInformationMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,21,3,2))
colubrisUsageInformationMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,21,3,2,1))
colubrisUsageInformationMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:colubrisUsageInformationMIBGroup.setStatus(_A)
colubrisUsageInformationMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,21,3,1,1))
colubrisUsageInformationMIBCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:colubrisUsageInformationMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisUsageInformationMIB':colubrisUsageInformationMIB,'colubrisUsageInformationMIBObjects':colubrisUsageInformationMIBObjects,'coUsageInformationGroup':coUsageInformationGroup,_E:coUsInfoUpTime,_F:coUsInfoLoadAverage1Min,_G:coUsInfoLoadAverage5Min,_H:coUsInfoLoadAverage15Min,_I:coUsInfoCpuUseNow,_J:coUsInfoCpuUse5Sec,_K:coUsInfoCpuUse10Sec,_L:coUsInfoCpuUse20Sec,_M:coUsInfoRamTotal,_N:coUsInfoRamFree,_O:coUsInfoRamBuffer,_P:coUsInfoRamCached,_Q:coUsInfoStorageUsePermanent,_R:coUsInfoStorageUseTemporary,'colubrisUsageInformationMIBNotificationPrefix':colubrisUsageInformationMIBNotificationPrefix,'colubrisUsageInformationMIBNotifications':colubrisUsageInformationMIBNotifications,'colubrisUsageInformationMIBConformance':colubrisUsageInformationMIBConformance,'colubrisUsageInformationMIBCompliances':colubrisUsageInformationMIBCompliances,'colubrisUsageInformationMIBCompliance':colubrisUsageInformationMIBCompliance,'colubrisUsageInformationMIBGroups':colubrisUsageInformationMIBGroups,_S:colubrisUsageInformationMIBGroup})