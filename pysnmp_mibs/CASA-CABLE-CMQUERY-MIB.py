_M='casaCmQueryroup'
_L='casaQueryCmtsSigQSignalNoise'
_K='casaQueryCmSigQSignalNoise'
_J='casaQueryCmStatusRxPower'
_I='casaQueryCmStatusTxPower'
_H='casaQueryCmMicroReflection'
_G='casaQueryCmTxTimeOffset'
_F='casaQueryCmIpAddress'
_E='casaQueryCmMacAddress'
_D='Integer32'
_C='read-only'
_B='CASA-CABLE-CMQUERY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
casa,=mibBuilder.importSymbols('CASA-MIB','casa')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
casaCmQueryMib=ModuleIdentity((1,3,6,1,4,1,20858,10,18))
class TenthdBmV(TextualConvention,Integer32):status=_A;displayHint='d-1'
class TenthdB(TextualConvention,Integer32):status=_A;displayHint='d-1'
_CasaMgmt_ObjectIdentity=ObjectIdentity
casaMgmt=_CasaMgmt_ObjectIdentity((1,3,6,1,4,1,20858,10))
_CasaCmQueryMibObjects_ObjectIdentity=ObjectIdentity
casaCmQueryMibObjects=_CasaCmQueryMibObjects_ObjectIdentity((1,3,6,1,4,1,20858,10,18,1))
_CasaCmQueryTable_Object=MibTable
casaCmQueryTable=_CasaCmQueryTable_Object((1,3,6,1,4,1,20858,10,18,1,1))
if mibBuilder.loadTexts:casaCmQueryTable.setStatus(_A)
_CasaCmQueryEntry_Object=MibTableRow
casaCmQueryEntry=_CasaCmQueryEntry_Object((1,3,6,1,4,1,20858,10,18,1,1,1))
casaCmQueryEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:casaCmQueryEntry.setStatus(_A)
_CasaQueryCmMacAddress_Type=MacAddress
_CasaQueryCmMacAddress_Object=MibTableColumn
casaQueryCmMacAddress=_CasaQueryCmMacAddress_Object((1,3,6,1,4,1,20858,10,18,1,1,1,1),_CasaQueryCmMacAddress_Type())
casaQueryCmMacAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:casaQueryCmMacAddress.setStatus(_A)
_CasaQueryCmIpAddress_Type=IpAddress
_CasaQueryCmIpAddress_Object=MibTableColumn
casaQueryCmIpAddress=_CasaQueryCmIpAddress_Object((1,3,6,1,4,1,20858,10,18,1,1,1,2),_CasaQueryCmIpAddress_Type())
casaQueryCmIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:casaQueryCmIpAddress.setStatus(_A)
_CasaQueryCmTxTimeOffset_Type=Unsigned32
_CasaQueryCmTxTimeOffset_Object=MibTableColumn
casaQueryCmTxTimeOffset=_CasaQueryCmTxTimeOffset_Object((1,3,6,1,4,1,20858,10,18,1,1,1,3),_CasaQueryCmTxTimeOffset_Type())
casaQueryCmTxTimeOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:casaQueryCmTxTimeOffset.setStatus(_A)
class _CasaQueryCmMicroReflection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CasaQueryCmMicroReflection_Type.__name__=_D
_CasaQueryCmMicroReflection_Object=MibTableColumn
casaQueryCmMicroReflection=_CasaQueryCmMicroReflection_Object((1,3,6,1,4,1,20858,10,18,1,1,1,4),_CasaQueryCmMicroReflection_Type())
casaQueryCmMicroReflection.setMaxAccess(_C)
if mibBuilder.loadTexts:casaQueryCmMicroReflection.setStatus(_A)
if mibBuilder.loadTexts:casaQueryCmMicroReflection.setUnits('dBc')
_CasaQueryCmStatusTxPower_Type=TenthdBmV
_CasaQueryCmStatusTxPower_Object=MibTableColumn
casaQueryCmStatusTxPower=_CasaQueryCmStatusTxPower_Object((1,3,6,1,4,1,20858,10,18,1,1,1,5),_CasaQueryCmStatusTxPower_Type())
casaQueryCmStatusTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:casaQueryCmStatusTxPower.setStatus(_A)
if mibBuilder.loadTexts:casaQueryCmStatusTxPower.setUnits('dBmV')
_CasaQueryCmStatusRxPower_Type=TenthdBmV
_CasaQueryCmStatusRxPower_Object=MibTableColumn
casaQueryCmStatusRxPower=_CasaQueryCmStatusRxPower_Object((1,3,6,1,4,1,20858,10,18,1,1,1,6),_CasaQueryCmStatusRxPower_Type())
casaQueryCmStatusRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:casaQueryCmStatusRxPower.setStatus(_A)
if mibBuilder.loadTexts:casaQueryCmStatusRxPower.setUnits('dBmV')
_CasaQueryCmSigQSignalNoise_Type=TenthdB
_CasaQueryCmSigQSignalNoise_Object=MibTableColumn
casaQueryCmSigQSignalNoise=_CasaQueryCmSigQSignalNoise_Object((1,3,6,1,4,1,20858,10,18,1,1,1,7),_CasaQueryCmSigQSignalNoise_Type())
casaQueryCmSigQSignalNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:casaQueryCmSigQSignalNoise.setStatus(_A)
if mibBuilder.loadTexts:casaQueryCmSigQSignalNoise.setUnits('dB')
_CasaQueryCmtsSigQSignalNoise_Type=TenthdB
_CasaQueryCmtsSigQSignalNoise_Object=MibTableColumn
casaQueryCmtsSigQSignalNoise=_CasaQueryCmtsSigQSignalNoise_Object((1,3,6,1,4,1,20858,10,18,1,1,1,8),_CasaQueryCmtsSigQSignalNoise_Type())
casaQueryCmtsSigQSignalNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:casaQueryCmtsSigQSignalNoise.setStatus(_A)
if mibBuilder.loadTexts:casaQueryCmtsSigQSignalNoise.setUnits('dB')
_CasaCmQueryGroups_ObjectIdentity=ObjectIdentity
casaCmQueryGroups=_CasaCmQueryGroups_ObjectIdentity((1,3,6,1,4,1,20858,10,18,2))
_CasaCmQueryCompliances_ObjectIdentity=ObjectIdentity
casaCmQueryCompliances=_CasaCmQueryCompliances_ObjectIdentity((1,3,6,1,4,1,20858,10,18,3))
casaCmQueryroup=ObjectGroup((1,3,6,1,4,1,20858,10,18,2,1))
casaCmQueryroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:casaCmQueryroup.setStatus(_A)
casaCmQueryCompliance=ModuleCompliance((1,3,6,1,4,1,20858,10,18,3,1))
casaCmQueryCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:casaCmQueryCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TenthdBmV':TenthdBmV,'TenthdB':TenthdB,'casaMgmt':casaMgmt,'casaCmQueryMib':casaCmQueryMib,'casaCmQueryMibObjects':casaCmQueryMibObjects,'casaCmQueryTable':casaCmQueryTable,'casaCmQueryEntry':casaCmQueryEntry,_E:casaQueryCmMacAddress,_F:casaQueryCmIpAddress,_G:casaQueryCmTxTimeOffset,_H:casaQueryCmMicroReflection,_I:casaQueryCmStatusTxPower,_J:casaQueryCmStatusRxPower,_K:casaQueryCmSigQSignalNoise,_L:casaQueryCmtsSigQSignalNoise,'casaCmQueryGroups':casaCmQueryGroups,_M:casaCmQueryroup,'casaCmQueryCompliances':casaCmQueryCompliances,'casaCmQueryCompliance':casaCmQueryCompliance})