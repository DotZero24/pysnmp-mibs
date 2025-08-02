_J='zhonePwBundleIsdnMode'
_I='zhonePwBundleTos'
_H='zhonePwBundleRowStatus'
_G='zhonePwBundleDs0Bundle'
_F='zhonePwBundleLocalIpAddr'
_E='zhonePwBundlePwIndex'
_D='Integer32'
_C='read-create'
_B='ZHONE-PW-BUNDLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zhoneModules,=mibBuilder.importSymbols('Zhone','zhoneModules')
zhonePwBundle=ModuleIdentity((1,3,6,1,4,1,5504,6,115))
if mibBuilder.loadTexts:zhonePwBundle.setRevisions(('2010-01-21 06:41','2008-08-18 06:50'))
_ZhonePwBundleTable_Object=MibTable
zhonePwBundleTable=_ZhonePwBundleTable_Object((1,3,6,1,4,1,5504,6,115,1))
if mibBuilder.loadTexts:zhonePwBundleTable.setStatus(_A)
_ZhonePwBundleEntry_Object=MibTableRow
zhonePwBundleEntry=_ZhonePwBundleEntry_Object((1,3,6,1,4,1,5504,6,115,1,1))
zhonePwBundleEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:zhonePwBundleEntry.setStatus(_A)
class _ZhonePwBundlePwIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhonePwBundlePwIndex_Type.__name__=_D
_ZhonePwBundlePwIndex_Object=MibTableColumn
zhonePwBundlePwIndex=_ZhonePwBundlePwIndex_Object((1,3,6,1,4,1,5504,6,115,1,1,1),_ZhonePwBundlePwIndex_Type())
zhonePwBundlePwIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhonePwBundlePwIndex.setStatus(_A)
_ZhonePwBundleLocalIpAddr_Type=IpAddress
_ZhonePwBundleLocalIpAddr_Object=MibTableColumn
zhonePwBundleLocalIpAddr=_ZhonePwBundleLocalIpAddr_Object((1,3,6,1,4,1,5504,6,115,1,1,2),_ZhonePwBundleLocalIpAddr_Type())
zhonePwBundleLocalIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePwBundleLocalIpAddr.setStatus(_A)
class _ZhonePwBundleDs0Bundle_Type(Bits):namedValues=NamedValues(*(('ds0-0',0),('ds0-1',1),('ds0-2',2),('ds0-3',3),('ds0-4',4),('ds0-5',5),('ds0-6',6),('ds0-7',7),('ds0-8',8),('ds0-9',9),('ds0-10',10),('ds0-11',11),('ds0-12',12),('ds0-13',13),('ds0-14',14),('ds0-15',15),('ds0-16',16),('ds0-17',17),('ds0-18',18),('ds0-19',19),('ds0-20',20),('ds0-21',21),('ds0-22',22),('ds0-23',23),('ds0-24',24),('ds0-25',25),('ds0-26',26),('ds0-27',27),('ds0-28',28),('ds0-29',29),('ds0-30',30),('ds0-31',31)))
_ZhonePwBundleDs0Bundle_Type.__name__='Bits'
_ZhonePwBundleDs0Bundle_Object=MibTableColumn
zhonePwBundleDs0Bundle=_ZhonePwBundleDs0Bundle_Object((1,3,6,1,4,1,5504,6,115,1,1,3),_ZhonePwBundleDs0Bundle_Type())
zhonePwBundleDs0Bundle.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePwBundleDs0Bundle.setStatus(_A)
_ZhonePwBundleRowStatus_Type=RowStatus
_ZhonePwBundleRowStatus_Object=MibTableColumn
zhonePwBundleRowStatus=_ZhonePwBundleRowStatus_Object((1,3,6,1,4,1,5504,6,115,1,1,4),_ZhonePwBundleRowStatus_Type())
zhonePwBundleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePwBundleRowStatus.setStatus(_A)
class _ZhonePwBundleTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhonePwBundleTos_Type.__name__=_D
_ZhonePwBundleTos_Object=MibTableColumn
zhonePwBundleTos=_ZhonePwBundleTos_Object((1,3,6,1,4,1,5504,6,115,1,1,5),_ZhonePwBundleTos_Type())
zhonePwBundleTos.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePwBundleTos.setStatus(_A)
class _ZhonePwBundleIsdnMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('lt',2),('nt1',3)))
_ZhonePwBundleIsdnMode_Type.__name__=_D
_ZhonePwBundleIsdnMode_Object=MibTableColumn
zhonePwBundleIsdnMode=_ZhonePwBundleIsdnMode_Object((1,3,6,1,4,1,5504,6,115,1,1,6),_ZhonePwBundleIsdnMode_Type())
zhonePwBundleIsdnMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePwBundleIsdnMode.setStatus(_A)
zhonePwBundleGroup=ObjectGroup((1,3,6,1,4,1,5504,6,115,2))
zhonePwBundleGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:zhonePwBundleGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhonePwBundle':zhonePwBundle,'zhonePwBundleTable':zhonePwBundleTable,'zhonePwBundleEntry':zhonePwBundleEntry,_E:zhonePwBundlePwIndex,_F:zhonePwBundleLocalIpAddr,_G:zhonePwBundleDs0Bundle,_H:zhonePwBundleRowStatus,_I:zhonePwBundleTos,_J:zhonePwBundleIsdnMode,'zhonePwBundleGroup':zhonePwBundleGroup})