_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percent,=mibBuilder.importSymbols('FS-NMS-QOS-PIB-MIB','Percent')
nmsMgmt,=mibBuilder.importSymbols('FS-NMS-SMI','nmsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
nmsMemoryPoolMIB=ModuleIdentity((1,3,6,1,4,1,52642,9,48))
if mibBuilder.loadTexts:nmsMemoryPoolMIB.setRevisions(('2003-10-16 00:00',))
_NmsMemoryPoolUtilization_Type=Percent
_NmsMemoryPoolUtilization_Object=MibScalar
nmsMemoryPoolUtilization=_NmsMemoryPoolUtilization_Object((1,3,6,1,4,1,52642,9,48,1),_NmsMemoryPoolUtilization_Type())
nmsMemoryPoolUtilization.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolUtilization.setStatus(_B)
_NmsMemoryPoolTotalMemorySize_Type=Unsigned32
_NmsMemoryPoolTotalMemorySize_Object=MibScalar
nmsMemoryPoolTotalMemorySize=_NmsMemoryPoolTotalMemorySize_Object((1,3,6,1,4,1,52642,9,48,2),_NmsMemoryPoolTotalMemorySize_Type())
nmsMemoryPoolTotalMemorySize.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolTotalMemorySize.setStatus(_B)
_NmsMemoryPoolImageRatio_Type=Percent
_NmsMemoryPoolImageRatio_Object=MibScalar
nmsMemoryPoolImageRatio=_NmsMemoryPoolImageRatio_Object((1,3,6,1,4,1,52642,9,48,3),_NmsMemoryPoolImageRatio_Type())
nmsMemoryPoolImageRatio.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolImageRatio.setStatus(_B)
_NmsMemoryPoolRegionRatio_Type=Percent
_NmsMemoryPoolRegionRatio_Object=MibScalar
nmsMemoryPoolRegionRatio=_NmsMemoryPoolRegionRatio_Object((1,3,6,1,4,1,52642,9,48,4),_NmsMemoryPoolRegionRatio_Type())
nmsMemoryPoolRegionRatio.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolRegionRatio.setStatus(_B)
_NmsMemoryPoolHeapRatio_Type=Percent
_NmsMemoryPoolHeapRatio_Object=MibScalar
nmsMemoryPoolHeapRatio=_NmsMemoryPoolHeapRatio_Object((1,3,6,1,4,1,52642,9,48,5),_NmsMemoryPoolHeapRatio_Type())
nmsMemoryPoolHeapRatio.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolHeapRatio.setStatus(_B)
_NmsMemoryPoolHeapUtilization_Type=Percent
_NmsMemoryPoolHeapUtilization_Object=MibScalar
nmsMemoryPoolHeapUtilization=_NmsMemoryPoolHeapUtilization_Object((1,3,6,1,4,1,52642,9,48,6),_NmsMemoryPoolHeapUtilization_Type())
nmsMemoryPoolHeapUtilization.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolHeapUtilization.setStatus(_B)
_NmsMemoryPoolMessageBufferRatio_Type=Percent
_NmsMemoryPoolMessageBufferRatio_Object=MibScalar
nmsMemoryPoolMessageBufferRatio=_NmsMemoryPoolMessageBufferRatio_Object((1,3,6,1,4,1,52642,9,48,7),_NmsMemoryPoolMessageBufferRatio_Type())
nmsMemoryPoolMessageBufferRatio.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolMessageBufferRatio.setStatus(_B)
_NmsMemoryPoolMessageBufferUtilization_Type=Percent
_NmsMemoryPoolMessageBufferUtilization_Object=MibScalar
nmsMemoryPoolMessageBufferUtilization=_NmsMemoryPoolMessageBufferUtilization_Object((1,3,6,1,4,1,52642,9,48,8),_NmsMemoryPoolMessageBufferUtilization_Type())
nmsMemoryPoolMessageBufferUtilization.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolMessageBufferUtilization.setStatus(_B)
_NmsMemoryPoolTotalFlashSize_Type=Percent
_NmsMemoryPoolTotalFlashSize_Object=MibScalar
nmsMemoryPoolTotalFlashSize=_NmsMemoryPoolTotalFlashSize_Object((1,3,6,1,4,1,52642,9,48,9),_NmsMemoryPoolTotalFlashSize_Type())
nmsMemoryPoolTotalFlashSize.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsMemoryPoolTotalFlashSize.setStatus(_B)
_NmsMemoryPoolNotifications_ObjectIdentity=ObjectIdentity
nmsMemoryPoolNotifications=_NmsMemoryPoolNotifications_ObjectIdentity((1,3,6,1,4,1,52642,9,48,20))
_NmsMemoryPoolConformance_ObjectIdentity=ObjectIdentity
nmsMemoryPoolConformance=_NmsMemoryPoolConformance_ObjectIdentity((1,3,6,1,4,1,52642,9,48,21))
_NmsMemoryPoolCompliances_ObjectIdentity=ObjectIdentity
nmsMemoryPoolCompliances=_NmsMemoryPoolCompliances_ObjectIdentity((1,3,6,1,4,1,52642,9,48,21,1))
_NmsMemoryPoolGroups_ObjectIdentity=ObjectIdentity
nmsMemoryPoolGroups=_NmsMemoryPoolGroups_ObjectIdentity((1,3,6,1,4,1,52642,9,48,21,2))
mibBuilder.exportSymbols('FS-NMS-MEMORY-POOL-MIB',**{'nmsMemoryPoolMIB':nmsMemoryPoolMIB,'nmsMemoryPoolUtilization':nmsMemoryPoolUtilization,'nmsMemoryPoolTotalMemorySize':nmsMemoryPoolTotalMemorySize,'nmsMemoryPoolImageRatio':nmsMemoryPoolImageRatio,'nmsMemoryPoolRegionRatio':nmsMemoryPoolRegionRatio,'nmsMemoryPoolHeapRatio':nmsMemoryPoolHeapRatio,'nmsMemoryPoolHeapUtilization':nmsMemoryPoolHeapUtilization,'nmsMemoryPoolMessageBufferRatio':nmsMemoryPoolMessageBufferRatio,'nmsMemoryPoolMessageBufferUtilization':nmsMemoryPoolMessageBufferUtilization,'nmsMemoryPoolTotalFlashSize':nmsMemoryPoolTotalFlashSize,'nmsMemoryPoolNotifications':nmsMemoryPoolNotifications,'nmsMemoryPoolConformance':nmsMemoryPoolConformance,'nmsMemoryPoolCompliances':nmsMemoryPoolCompliances,'nmsMemoryPoolGroups':nmsMemoryPoolGroups})