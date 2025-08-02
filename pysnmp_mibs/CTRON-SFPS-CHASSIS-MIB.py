_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsChassisRipAPI,sfpsChassisRipTable=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsChassisRipAPI','sfpsChassisRipTable')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsChassisRipChassisMac_Type=OctetString
_SfpsChassisRipChassisMac_Object=MibScalar
sfpsChassisRipChassisMac=_SfpsChassisRipChassisMac_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,1,1),_SfpsChassisRipChassisMac_Type())
sfpsChassisRipChassisMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRipChassisMac.setStatus(_A)
_SfpsChassisRipFPPortMask_Type=OctetString
_SfpsChassisRipFPPortMask_Object=MibScalar
sfpsChassisRipFPPortMask=_SfpsChassisRipFPPortMask_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,1,2),_SfpsChassisRipFPPortMask_Type())
sfpsChassisRipFPPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRipFPPortMask.setStatus(_A)
_SfpsChassisRipINBPortMask_Type=OctetString
_SfpsChassisRipINBPortMask_Object=MibScalar
sfpsChassisRipINBPortMask=_SfpsChassisRipINBPortMask_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,1,3),_SfpsChassisRipINBPortMask_Type())
sfpsChassisRipINBPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRipINBPortMask.setStatus(_A)
_SfpsChassisRipModifiedTime_Type=TimeTicks
_SfpsChassisRipModifiedTime_Object=MibScalar
sfpsChassisRipModifiedTime=_SfpsChassisRipModifiedTime_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,1,4),_SfpsChassisRipModifiedTime_Type())
sfpsChassisRipModifiedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRipModifiedTime.setStatus(_A)
class _SfpsChassisRipStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('active',2),('dead',3)))
_SfpsChassisRipStatus_Type.__name__=_D
_SfpsChassisRipStatus_Object=MibScalar
sfpsChassisRipStatus=_SfpsChassisRipStatus_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,1,5),_SfpsChassisRipStatus_Type())
sfpsChassisRipStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRipStatus.setStatus(_A)
class _SfpsChassisRipAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('add',2),('delete',3),('purgePort',4),('sendUpdate',5),('clearTable',6),('setTimer',7)))
_SfpsChassisRipAPIVerb_Type.__name__=_D
_SfpsChassisRipAPIVerb_Object=MibScalar
sfpsChassisRipAPIVerb=_SfpsChassisRipAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,2,1),_SfpsChassisRipAPIVerb_Type())
sfpsChassisRipAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsChassisRipAPIVerb.setStatus(_A)
_SfpsChassisRipAPIChassisMac_Type=SfpsAddress
_SfpsChassisRipAPIChassisMac_Object=MibScalar
sfpsChassisRipAPIChassisMac=_SfpsChassisRipAPIChassisMac_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,2,2),_SfpsChassisRipAPIChassisMac_Type())
sfpsChassisRipAPIChassisMac.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsChassisRipAPIChassisMac.setStatus(_A)
_SfpsChassisRipAPIPort_Type=Integer32
_SfpsChassisRipAPIPort_Object=MibScalar
sfpsChassisRipAPIPort=_SfpsChassisRipAPIPort_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,2,3),_SfpsChassisRipAPIPort_Type())
sfpsChassisRipAPIPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsChassisRipAPIPort.setStatus(_A)
_SfpsChassisRipAPITimer_Type=Integer32
_SfpsChassisRipAPITimer_Object=MibScalar
sfpsChassisRipAPITimer=_SfpsChassisRipAPITimer_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,2,4),_SfpsChassisRipAPITimer_Type())
sfpsChassisRipAPITimer.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsChassisRipAPITimer.setStatus(_A)
_SfpsChassisRipAPINumInTable_Type=Integer32
_SfpsChassisRipAPINumInTable_Object=MibScalar
sfpsChassisRipAPINumInTable=_SfpsChassisRipAPINumInTable_Object((1,3,6,1,4,1,52,4,2,4,2,6,1,2,5),_SfpsChassisRipAPINumInTable_Type())
sfpsChassisRipAPINumInTable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRipAPINumInTable.setStatus(_A)
mibBuilder.exportSymbols('CTRON-SFPS-CHASSIS-MIB',**{'SfpsAddress':SfpsAddress,'sfpsChassisRipChassisMac':sfpsChassisRipChassisMac,'sfpsChassisRipFPPortMask':sfpsChassisRipFPPortMask,'sfpsChassisRipINBPortMask':sfpsChassisRipINBPortMask,'sfpsChassisRipModifiedTime':sfpsChassisRipModifiedTime,'sfpsChassisRipStatus':sfpsChassisRipStatus,'sfpsChassisRipAPIVerb':sfpsChassisRipAPIVerb,'sfpsChassisRipAPIChassisMac':sfpsChassisRipAPIChassisMac,'sfpsChassisRipAPIPort':sfpsChassisRipAPIPort,'sfpsChassisRipAPITimer':sfpsChassisRipAPITimer,'sfpsChassisRipAPINumInTable':sfpsChassisRipAPINumInTable})