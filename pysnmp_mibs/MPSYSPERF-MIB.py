_C='current'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mpSysPerfMib=ModuleIdentity((1,3,6,1,4,1,5651,3,901))
class _MpSysRamUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MpSysRamUsage_Type.__name__=_A
_MpSysRamUsage_Object=MibScalar
mpSysRamUsage=_MpSysRamUsage_Object((1,3,6,1,4,1,5651,3,901,1),_MpSysRamUsage_Type())
mpSysRamUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:mpSysRamUsage.setStatus(_C)
class _MpSysCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MpSysCpuUsage_Type.__name__=_A
_MpSysCpuUsage_Object=MibScalar
mpSysCpuUsage=_MpSysCpuUsage_Object((1,3,6,1,4,1,5651,3,901,2),_MpSysCpuUsage_Type())
mpSysCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:mpSysCpuUsage.setStatus(_C)
class _MpSysCpuPeakLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MpSysCpuPeakLoad_Type.__name__=_A
_MpSysCpuPeakLoad_Object=MibScalar
mpSysCpuPeakLoad=_MpSysCpuPeakLoad_Object((1,3,6,1,4,1,5651,3,901,3),_MpSysCpuPeakLoad_Type())
mpSysCpuPeakLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:mpSysCpuPeakLoad.setStatus(_C)
mibBuilder.exportSymbols('MPSYSPERF-MIB',**{'mpSysPerfMib':mpSysPerfMib,'mpSysRamUsage':mpSysRamUsage,'mpSysCpuUsage':mpSysCpuUsage,'mpSysCpuPeakLoad':mpSysCpuPeakLoad})