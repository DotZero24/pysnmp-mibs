_S='eMSLicenseLimit'
_R='eMSLicense'
_Q='eMSDataRatioLimit'
_P='eMSDataUsed'
_O='eMSDataSize'
_N='eMSDiskRatioLimit'
_M='eMSDiskUsed'
_L='eMSDiskSize'
_K='eMSMemoryRatioLimit'
_J='eMSMemoryUsed'
_I='eMSMemorySize'
_H='eMSCPURatioLimit'
_G='eMSCPURatio'
_F='eMSProcessLimit'
_E='eMSProcess'
_D='MB'
_C='accessible-for-notify'
_B='NMS-EMSTRAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsWorkGroup,=mibBuilder.importSymbols('NMS-SMI','nmsWorkGroup')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eMSMibModule=ModuleIdentity((1,3,6,1,4,1,3320,20,1))
_EMSTrapObject_ObjectIdentity=ObjectIdentity
eMSTrapObject=_EMSTrapObject_ObjectIdentity((1,3,6,1,4,1,3320,20,1,1))
_EMSTrap_ObjectIdentity=ObjectIdentity
eMSTrap=_EMSTrap_ObjectIdentity((1,3,6,1,4,1,3320,20,1,1,1))
_EMSTrapInfo_ObjectIdentity=ObjectIdentity
eMSTrapInfo=_EMSTrapInfo_ObjectIdentity((1,3,6,1,4,1,3320,20,1,1,3))
_EMSProcess_Type=Integer32
_EMSProcess_Object=MibScalar
eMSProcess=_EMSProcess_Object((1,3,6,1,4,1,3320,20,1,1,3,1),_EMSProcess_Type())
eMSProcess.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSProcess.setStatus(_A)
_EMSProcessLimit_Type=Integer32
_EMSProcessLimit_Object=MibScalar
eMSProcessLimit=_EMSProcessLimit_Object((1,3,6,1,4,1,3320,20,1,1,3,2),_EMSProcessLimit_Type())
eMSProcessLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSProcessLimit.setStatus(_A)
if mibBuilder.loadTexts:eMSProcessLimit.setUnits('%')
_EMSCPURatio_Type=Integer32
_EMSCPURatio_Object=MibScalar
eMSCPURatio=_EMSCPURatio_Object((1,3,6,1,4,1,3320,20,1,1,3,3),_EMSCPURatio_Type())
eMSCPURatio.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSCPURatio.setStatus(_A)
if mibBuilder.loadTexts:eMSCPURatio.setUnits('%')
_EMSCPURatioLimit_Type=Integer32
_EMSCPURatioLimit_Object=MibScalar
eMSCPURatioLimit=_EMSCPURatioLimit_Object((1,3,6,1,4,1,3320,20,1,1,3,4),_EMSCPURatioLimit_Type())
eMSCPURatioLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSCPURatioLimit.setStatus(_A)
if mibBuilder.loadTexts:eMSCPURatioLimit.setUnits('%')
_EMSMemorySize_Type=Integer32
_EMSMemorySize_Object=MibScalar
eMSMemorySize=_EMSMemorySize_Object((1,3,6,1,4,1,3320,20,1,1,3,5),_EMSMemorySize_Type())
eMSMemorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSMemorySize.setStatus(_A)
if mibBuilder.loadTexts:eMSMemorySize.setUnits(_D)
_EMSMemoryUsed_Type=Integer32
_EMSMemoryUsed_Object=MibScalar
eMSMemoryUsed=_EMSMemoryUsed_Object((1,3,6,1,4,1,3320,20,1,1,3,6),_EMSMemoryUsed_Type())
eMSMemoryUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSMemoryUsed.setStatus(_A)
if mibBuilder.loadTexts:eMSMemoryUsed.setUnits(_D)
_EMSMemoryRatioLimit_Type=Integer32
_EMSMemoryRatioLimit_Object=MibScalar
eMSMemoryRatioLimit=_EMSMemoryRatioLimit_Object((1,3,6,1,4,1,3320,20,1,1,3,7),_EMSMemoryRatioLimit_Type())
eMSMemoryRatioLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSMemoryRatioLimit.setStatus(_A)
if mibBuilder.loadTexts:eMSMemoryRatioLimit.setUnits('%')
_EMSDiskSize_Type=Integer32
_EMSDiskSize_Object=MibScalar
eMSDiskSize=_EMSDiskSize_Object((1,3,6,1,4,1,3320,20,1,1,3,8),_EMSDiskSize_Type())
eMSDiskSize.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSDiskSize.setStatus(_A)
if mibBuilder.loadTexts:eMSDiskSize.setUnits(_D)
_EMSDiskUsed_Type=Integer32
_EMSDiskUsed_Object=MibScalar
eMSDiskUsed=_EMSDiskUsed_Object((1,3,6,1,4,1,3320,20,1,1,3,9),_EMSDiskUsed_Type())
eMSDiskUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSDiskUsed.setStatus(_A)
if mibBuilder.loadTexts:eMSDiskUsed.setUnits(_D)
_EMSDiskRatioLimit_Type=Integer32
_EMSDiskRatioLimit_Object=MibScalar
eMSDiskRatioLimit=_EMSDiskRatioLimit_Object((1,3,6,1,4,1,3320,20,1,1,3,10),_EMSDiskRatioLimit_Type())
eMSDiskRatioLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSDiskRatioLimit.setStatus(_A)
if mibBuilder.loadTexts:eMSDiskRatioLimit.setUnits('%')
_EMSDataSize_Type=Integer32
_EMSDataSize_Object=MibScalar
eMSDataSize=_EMSDataSize_Object((1,3,6,1,4,1,3320,20,1,1,3,11),_EMSDataSize_Type())
eMSDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSDataSize.setStatus(_A)
if mibBuilder.loadTexts:eMSDataSize.setUnits(_D)
_EMSDataUsed_Type=Integer32
_EMSDataUsed_Object=MibScalar
eMSDataUsed=_EMSDataUsed_Object((1,3,6,1,4,1,3320,20,1,1,3,12),_EMSDataUsed_Type())
eMSDataUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSDataUsed.setStatus(_A)
if mibBuilder.loadTexts:eMSDataUsed.setUnits(_D)
_EMSDataRatioLimit_Type=Integer32
_EMSDataRatioLimit_Object=MibScalar
eMSDataRatioLimit=_EMSDataRatioLimit_Object((1,3,6,1,4,1,3320,20,1,1,3,13),_EMSDataRatioLimit_Type())
eMSDataRatioLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSDataRatioLimit.setStatus(_A)
if mibBuilder.loadTexts:eMSDataRatioLimit.setUnits('%')
_EMSLicense_Type=Integer32
_EMSLicense_Object=MibScalar
eMSLicense=_EMSLicense_Object((1,3,6,1,4,1,3320,20,1,1,3,14),_EMSLicense_Type())
eMSLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSLicense.setStatus(_A)
_EMSLicenseLimit_Type=Integer32
_EMSLicenseLimit_Object=MibScalar
eMSLicenseLimit=_EMSLicenseLimit_Object((1,3,6,1,4,1,3320,20,1,1,3,15),_EMSLicenseLimit_Type())
eMSLicenseLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:eMSLicenseLimit.setStatus(_A)
eMSProcessTrap=NotificationType((1,3,6,1,4,1,3320,20,1,1,1,1))
eMSProcessTrap.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:eMSProcessTrap.setStatus(_A)
eMSCPUTrap=NotificationType((1,3,6,1,4,1,3320,20,1,1,1,2))
eMSCPUTrap.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:eMSCPUTrap.setStatus(_A)
eMSMemoryTrap=NotificationType((1,3,6,1,4,1,3320,20,1,1,1,3))
eMSMemoryTrap.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:eMSMemoryTrap.setStatus(_A)
eMSDiskTrap=NotificationType((1,3,6,1,4,1,3320,20,1,1,1,4))
eMSDiskTrap.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:eMSDiskTrap.setStatus(_A)
eMSDataTrap=NotificationType((1,3,6,1,4,1,3320,20,1,1,1,5))
eMSDataTrap.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:eMSDataTrap.setStatus(_A)
eMSLicenseTrap=NotificationType((1,3,6,1,4,1,3320,20,1,1,1,6))
eMSLicenseTrap.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:eMSLicenseTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eMSMibModule':eMSMibModule,'eMSTrapObject':eMSTrapObject,'eMSTrap':eMSTrap,'eMSProcessTrap':eMSProcessTrap,'eMSCPUTrap':eMSCPUTrap,'eMSMemoryTrap':eMSMemoryTrap,'eMSDiskTrap':eMSDiskTrap,'eMSDataTrap':eMSDataTrap,'eMSLicenseTrap':eMSLicenseTrap,'eMSTrapInfo':eMSTrapInfo,_E:eMSProcess,_F:eMSProcessLimit,_G:eMSCPURatio,_H:eMSCPURatioLimit,_I:eMSMemorySize,_J:eMSMemoryUsed,_K:eMSMemoryRatioLimit,_L:eMSDiskSize,_M:eMSDiskUsed,_N:eMSDiskRatioLimit,_O:eMSDataSize,_P:eMSDataUsed,_Q:eMSDataRatioLimit,_R:eMSLicense,_S:eMSLicenseLimit})